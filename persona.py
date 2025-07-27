import os
import json
import fitz  # PyMuPDF
from pathlib import Path
from datetime import datetime


def load_input(input_path):
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_keywords(job_description):
    # Simple keyword extraction: words longer than 3 characters
    words = job_description.lower().replace(",", "").split()
    keywords = [word for word in words if len(word) > 3]
    return keywords


def extract_relevant_sections(pdf_path, keywords):
    doc = fitz.open(pdf_path)
    relevant = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")

        for block in blocks:
            text = block[4].strip()
            if not text:
                continue

            lower_text = text.lower()
            score = sum(kw in lower_text for kw in keywords)

            if score > 0:
                section_title = text.split("\n")[0][:80]
                relevant.append({
                    "document": os.path.basename(pdf_path),
                    "page": page_num + 1,
                    "section_title": section_title,
                    "refined_text": text,
                    "importance_score": score
                })

    return relevant


def rank_sections(all_sections):
    ranked = sorted(all_sections, key=lambda x: -x["importance_score"])
    top_sections = ranked[:5]

    extracted = []
    analysis = []

    for rank, sec in enumerate(top_sections, 1):
        extracted.append({
            "document": sec["document"],
            "section_title": sec["section_title"],
            "importance_rank": rank,
            "page_number": sec["page"]
        })

        analysis.append({
            "document": sec["document"],
            "refined_text": sec["refined_text"],
            "page_number": sec["page"]
        })

    return extracted, analysis


def main():
    input_file = Path("/app/input/challenge1b_input.json")
    base_dir = input_file.parent
    output_path = base_dir / "challenge1b_output.json"
    pdf_dir = base_dir / "PDFs"

    input_json = load_input(input_file)
    persona = input_json["persona"]["role"]
    job = input_json["job_to_be_done"]["task"]
    documents = input_json["documents"]

    keywords = get_keywords(job)
    all_sections = []

    for doc in documents:
        pdf_path = pdf_dir / doc["filename"]
        if not pdf_path.exists():
            print(f"❌ Warning: {pdf_path} not found.")
            continue
        all_sections.extend(extract_relevant_sections(pdf_path, keywords))

    extracted, analysis = rank_sections(all_sections)

    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in documents],
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted,
        "subsection_analysis": analysis
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("✅ challenge1b_output.json created at:", output_path)


# 🔧 Corrected entry point
if __name__ == "__main__":
    main()

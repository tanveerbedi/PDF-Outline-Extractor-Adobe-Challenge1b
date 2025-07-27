# PDF Outline Extractor - Adobe "Connecting the Dots" Challenge (Round 1B)

## Overview

This project was developed as part of **Adobe India Hackathon 2025 – Round 1B: Connecting the Dots Challenge**. It aims to convert traditional static PDFs into semantically structured, persona-driven insights by automatically analyzing and extracting the most relevant sections based on the reader’s intent or job-to-be-done.

The solution addresses real-world challenges like:

* Navigating lengthy and unstructured documents
* Extracting task-relevant content for distinct user personas (e.g., HR professionals, travel planners, chefs)
* Providing high-precision summaries and rankings from multi-page PDFs

Our system scales across multiple domains and datasets by utilizing keyword-driven scoring logic, document segmentation, and text ranking strategies.
It was tested on diverse domains such as travel itineraries, HR compliance documents, and food preparation manuals to simulate real-world workflows and deliver targeted outputs.

---

## 📁 Project Structure

```
Challenge_1b/
├── Collection 1/                    # Travel Planning
│   ├── PDFs/                       # South of France guides
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
├── Collection 2/                    # Adobe Acrobat Learning
│   ├── PDFs/                       # Acrobat tutorials
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
├── Collection 3/                    # Recipe Collection
│   ├── PDFs/                       # Cooking guides
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
└── README.md
```

---

## 🗓️ Collections

### Collection 1: Travel Planning

* **Challenge ID**: round\_1b\_002
* **Persona**: Travel Planner
* **Task**: Plan a 4-day trip for 10 college friends to South of France
* **Documents**: 7 travel guides

### Collection 2: Adobe Acrobat Learning

* **Challenge ID**: round\_1b\_003
* **Persona**: HR Professional
* **Task**: Create and manage fillable forms for onboarding and compliance
* **Documents**: 15 Acrobat guides

### Collection 3: Recipe Collection

* **Challenge ID**: round\_1b\_001
* **Persona**: Food Contractor
* **Task**: Prepare vegetarian buffet-style dinner menu for corporate gathering
* **Documents**: 9 cooking guides

---

## 🔄 Approach

This solution uses a lightweight rule-based keyword matching and importance scoring system to extract relevant sections from PDFs:

* Loads `persona` and `job_to_be_done` from input JSON.
* Generates keywords from the job/task description.
* For each PDF page, it:

  * Extracts blocks of text
  * Scores blocks based on keyword occurrence
  * Filters and ranks the most relevant sections
* Final output includes a ranked list of sections and detailed summaries.

---

## 🚀 How to Run This Project

### Prerequisites

* Python 3.8+
* PyMuPDF

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
PyMuPDF==1.23.7
scikit-learn==1.4.2
numpy==1.24.4
sentence-transformers==2.2.2
```

### 2. Project Folder Setup

Make sure your folder structure follows this:

```
Collection N/
├── PDFs/                  # folder with .pdf files
├── challenge1b_input.json
└── persona.py             # script provided
```

### 3. Run the script

```bash
python persona.py
```

Once complete, you'll get:

```
✅ challenge1b_output.json created at: ./Collection N/
```

---

## 📊 Requirements & Libraries Used

* **Python 3.8+**
* **PyMuPDF (fitz)** – PDF text parsing
* **scikit-learn** – optional for future ranking enhancements
* **numpy** – general utility
* **sentence-transformers** – for future semantic relevance upgrades
* **Standard Libraries**: `json`, `os`, `datetime`, `pathlib`

---

## 📄 Input/Output Format

### Input JSON

```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [{"filename": "doc.pdf", "title": "Title"}],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Use case description"}
}
```

### Output JSON

```json
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```

---

## 👨‍💼 Authors

Made with ❤️ by:

* **Tanveer Singh**
* **Sehajdeep Singh**
* **Tarun Bhatti**

All authors are final-year students from **Thapar Institute of Engineering and Technology**, Patiala.

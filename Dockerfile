# ✅ Base image
FROM python:3.10-slim

# ✅ Set working directory
WORKDIR /app

# ✅ Install only essential system dependencies (for PyMuPDF, transformers)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# ✅ Copy only requirements to cache pip install
COPY requirements.txt .

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy rest of the project files
COPY . .

# ✅ Set default script to run
CMD ["python", "persona.py"]

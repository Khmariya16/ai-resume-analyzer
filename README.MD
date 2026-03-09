# AI Resume Analyzer

An AI-powered resume analysis tool that evaluates resumes against job descriptions using NLP and machine learning techniques.

The system extracts skills from resumes, compares them with job requirements, calculates a match score, detects missing skills, and performs ATS keyword scanning.

---

## Features

* Resume parsing (PDF, DOCX, PNG, JPG)
* OCR-based text extraction for image resumes
* Skill extraction using spaCy NLP
* Resume–Job Description similarity scoring
* Skill gap detection
* ATS keyword scanning
* Resume improvement suggestions
* Interactive dashboard with charts

---

## Tech Stack

* Python
* Flask
* spaCy
* Scikit-learn
* Pandas
* Chart.js
* HTML/CSS

---

## Project Architecture

Resume Upload
↓
Resume Text Extraction
↓
Skill Extraction (spaCy NLP)
↓
Similarity Scoring (Cosine Similarity)
↓
Skill Gap Detection
↓
ATS Keyword Scan
↓
Dashboard Visualization

---

## Installation

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer
```

Create virtual environment

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Run the application

```
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

## Future Improvements

* Deploy using Docker
* Add deep learning based skill extraction
* Resume keyword highlighting
* Multi-language resume support
* Integration with LinkedIn job descriptions

---

## Author

Mariya Khan
B.Tech Computer Science

---

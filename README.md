# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes resumes and provides an ATS-style score based on the skills detected in the resume.

The application allows users to upload their resume in PDF or DOCX format and receive a quick analysis of their skills, missing skills, ATS score, and extracted resume text.

## 🚀 Features

- 📄 Upload resumes in PDF or DOCX format
- 📊 Generate an ATS-style resume score
- 🔍 Detect technical skills from the resume
- ✅ Display skills found in the resume
- ❌ Display skills missing from the predefined skill list
- 📝 Extract and display resume text
- 💻 Interactive Streamlit frontend
- ⚡ FastAPI backend for resume processing
- 🔗 Frontend and backend connected through REST API

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### Programming Language
- Python

### Libraries
- PyPDF
- python-docx
- Requests

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── backend/
│   └── main.py
│
├── fronted.py
├── .gitignore
└── README.md

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

⚙️ How It Works
User uploads a resume in PDF or DOCX format.
The Streamlit frontend sends the resume to the FastAPI backend.
The backend extracts the text from the resume.
The application checks the resume for predefined technical skills.
An ATS-style score is calculated based on the detected skills.
The results are displayed on the Streamlit interface.
📊 ATS Score

The current version calculates the score based on the percentage of predefined skills detected in the resume.

For example:

Skills detected: 8
Total skills checked: 16

ATS Score = 50%


🔮 Future Improvements
🤖 AI-powered resume analysis using LLMs
🎯 Job-description based resume matching
📈 Keyword optimization suggestions
💡 Personalized resume improvement recommendations
📊 Detailed ATS analysis
🧠 Experience and education section analysis
📄 Resume formatting analysis
🌐 Deploy the application online
🔐 User authentication and resume history
🎯 Project Goal

The goal of this project is to build a beginner-friendly resume analysis tool that helps students and job seekers understand how well their resumes match common technical skill requirements.

👩‍💻 Author

Esa Chanda

B.Tech Computer Science & Engineering
Institute of Engineering & Management

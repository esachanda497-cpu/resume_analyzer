from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
from docx import Document

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API"}


@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        contents = await file.read()

        with open("temp_resume.pdf", "wb") as f:
            f.write(contents)

        reader = PdfReader("temp_resume.pdf")
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

    elif filename.endswith(".docx"):
        contents = await file.read()

        with open("temp_resume.docx", "wb") as f:
            f.write(contents)

        document = Document("temp_resume.docx")

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

    else:
        return {
            "error": "Only PDF and DOCX files are supported"
        }

    skills = [
        "python", "java", "c", "c++", "javascript",
        "html", "css", "sql", "machine learning",
        "data analysis", "git", "github", "fastapi",
        "django", "react"
    ]

    text_lower = text.lower()

    found_skills = []
    missing_skills = []

    for skill in skills:
        if skill in text_lower:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = int((len(found_skills) / len(skills)) * 100)

    return {
        "filename": file.filename,
        "text": text,
        "score": score,
        "skills_found": found_skills,
        "skills_missing": missing_skills
    }
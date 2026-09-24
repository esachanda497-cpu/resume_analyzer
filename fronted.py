import streamlit as st
import requests

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get a quick ATS-style analysis.")

file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "💼 Paste the Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

if file:

    st.success(f"Selected: {file.name}")

    if st.button("🔍 Analyze Resume"):

        if not job_description.strip():
            st.warning("Please paste a job description first.")
            st.stop()

        files = {
            "file": (
                file.name,
                file.getvalue(),
                file.type
            )
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files=files
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Resume analyzed successfully!")

                st.divider()

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "ATS Score",
                        f"{data['score']}/100"
                    )

                with col2:
                    st.metric(
                        "Skills Found",
                        len(data["skills_found"])
                    )

                st.subheader("✅ Skills Found")

                if data["skills_found"]:
                    st.write(
                        ", ".join(
                            skill.title()
                            for skill in data["skills_found"]
                        )
                    )
                else:
                    st.write("No matching skills detected.")

                st.subheader("⚠️ Skills Missing")

                if data["skills_missing"]:
                    st.write(
                        ", ".join(
                            skill.title()
                            for skill in data["skills_missing"]
                        )
                    )
                else:
                    st.write("No missing skills detected.")

                st.subheader("📄 Extracted Resume Text")

                st.text_area(
                    "Resume Content",
                    data["text"],
                    height=400
                )

            else:
                st.error(
                    f"Backend returned error: {response.status_code}"
                )

        except Exception as e:
            st.error(f"Could not connect to backend: {e}")
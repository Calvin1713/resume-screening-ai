import streamlit as st

from utils.resume_parser import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.similarity import calculate_similarity
from utils.skill_gap import load_skills, skill_analysis

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("AI Resume Screening & Job Match Analyzer")

st.write(
    "Upload your resume and compare it with a job description."
)

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_resume is not None and job_description != "":

        resume_text = extract_text_from_pdf(uploaded_resume)

        clean_resume = preprocess_text(resume_text)

        clean_jd = preprocess_text(job_description)

        similarity_score = calculate_similarity(
            clean_resume,
            clean_jd
        )

        skills = load_skills("data/skills_database.txt")

        matched_skills, missing_skills = skill_analysis(
            clean_resume,
            clean_jd,
            skills
        )

        st.subheader("Match Score")
        st.success(f"{similarity_score}% Match")

        st.subheader("Matched Skills")

        if matched_skills:
            for skill in matched_skills:
                st.write(f"✔ {skill}")
        else:
            st.write("No matching skills found.")

        st.subheader("Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.write(f"✘ {skill}")
        else:
            st.write("No missing skills.")

    else:
        st.warning(
            "Please upload a resume and paste a job description."
        )
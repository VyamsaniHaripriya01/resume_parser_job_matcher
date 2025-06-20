import streamlit as st
import os
import sys
import pandas as pd

# Add scripts path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
scripts_path = os.path.join(project_root, "scripts")
sys.path.append(scripts_path)

from parse_resume import extract_text_from_docx, extract_text_from_pdf, extract_candidate_info
from text_cleaner import clean_text
from job_matcher import get_bert_similarity, extract_top_keywords

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("📄 Resume & JD Matcher using BERT")

st.markdown("Upload a resume and job description (.docx) to see candidate info, similarity score, and matched keywords.")

resume_file = st.file_uploader("📎 Upload Resume (.docx or .pdf)", type=["docx", "pdf"])
jd_file = st.file_uploader("📄 Upload Job Description (.docx or .pdf)", type=["docx", "pdf"])

if resume_file and jd_file:
    # Save uploaded files temporarily
    resume_path = f"temp_resume.{resume_file.name.split('.')[-1]}"
    jd_path = f"temp_jd.{jd_file.name.split('.')[-1]}"

    with open(resume_path, "wb") as f:
        f.write(resume_file.read())

    with open(jd_path, "wb") as f:
        f.write(jd_file.read())

    # Extract text depending on file type From Resume
    try:
        if resume_file.type == "application/pdf":
            resume_raw = extract_text_from_pdf(resume_path)
        else:
            resume_raw = extract_text_from_docx(resume_path)
    except ValueError as e:
        st.error(f"❌ Resume Error: {e}")
        st.stop()
        
    # Extract text depending on file type From Resume
    try:
        if jd_file.type == "application/pdf":
            jd_raw = extract_text_from_pdf(jd_path)
        else:
            jd_raw = extract_text_from_docx(jd_path)
    except ValueError as e:
        st.error(f"❌ JD Error: {e}")
        st.stop()

    # Clean text
    resume_cleaned = clean_text(resume_raw)
    jd_cleaned = clean_text(jd_raw)

    # Process and match
    info = extract_candidate_info(resume_raw)
    score = get_bert_similarity(resume_cleaned, jd_cleaned)

    jd_keywords = extract_top_keywords(jd_cleaned, top_n=10)
    matched_keywords = [kw for kw in jd_keywords if kw.lower() in resume_cleaned.lower()]


    # Layout: Two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👤 Candidate Info")
        st.write(f"**Name:** {info.get('name')}")
        st.write(f"**Email:** {info.get('email')}")
        st.write(f"**Phone:** {info.get('phone')}")
        st.write(f"**Experience:** {' | '.join(info.get('experience_summary', []))}")

    with col2:
        st.subheader("🎯 Match Score")
        st.metric("BERT Similarity", f"{score} %")
        st.subheader("🔍 Matched JD Keywords")
        st.write(", ".join(matched_keywords) or "No matches found.")

    # Downloadable report
    st.subheader("📥 Download Report")
    result_df = pd.DataFrame({
        "Candidate Name": [info.get("name")],
        "Email": [info.get("email")],
        "Phone": [info.get("phone")],
        "Match Score (%)": [score],
        "Matched Keywords": [", ".join(matched_keywords)]
    })

    csv = result_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Result as CSV", csv, "match_result.csv", "text/csv")

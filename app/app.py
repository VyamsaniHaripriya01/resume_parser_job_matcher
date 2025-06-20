import streamlit as st
import os
import sys
import pandas as pd

# Add scripts path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
scripts_path = os.path.join(project_root, "scripts")
sys.path.append(scripts_path)

from parse_resume import extract_text_from_docx, extract_candidate_info
from text_cleaner import clean_text
from job_matcher import get_bert_similarity, extract_top_keywords

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("📄 Resume & JD Matcher using BERT")

st.markdown("Upload a resume and job description (.docx) to see candidate info, similarity score, and matched keywords.")

resume_file = st.file_uploader("📎 Upload Resume (.docx)", type=["docx"])
jd_file = st.file_uploader("📄 Upload Job Description (.docx)", type=["docx"])

if resume_file and jd_file:
    with open("temp_resume.docx", "wb") as f:
        f.write(resume_file.read())
    with open("temp_jd.docx", "wb") as f:
        f.write(jd_file.read())

    resume_raw = extract_text_from_docx("temp_resume.docx")
    jd_raw = extract_text_from_docx("temp_jd.docx")
    resume_cleaned = clean_text(resume_raw)
    jd_cleaned = clean_text(jd_raw)

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

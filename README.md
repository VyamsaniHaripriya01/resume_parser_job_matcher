# 📄 Resume & JD Matcher with BERT

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resume-parser-job-matcher-ml-nlp.streamlit.app/)
![GitHub last commit](https://img.shields.io/github/last-commit/VyamsaniHaripriya01/resume_parser_job_matcher)
![Repo Size](https://img.shields.io/github/repo-size/VyamsaniHaripriya01/resume_parser_job_matcher)
![License: Personal & Educational Use Only](https://img.shields.io/badge/license-Personal%20%26%20Educational%20Use-orange)


A smart NLP-powered Streamlit app to match resumes with job descriptions using semantic similarity.

## 🚀 Features
- Upload Resume (.docx) & JD (.docx)
- Extract candidate info (Name, Email, Phone, Experience)
- Compute semantic match score using BERT embeddings
- Extract important JD keywords and check if they’re present in the resume
- Download results as a CSV

## 📸 Demo Screenshot

![App Screenshot](screenshots/app_ui.png)

---

## 🧠 How It Works

1. Extracts text using `python-docx`
2. Cleans and processes text
3. Uses Sentence-BERT (`all-MiniLM-L6-v2`) to compute similarity
4. Uses TF-IDF to extract JD keywords
5. Displays info via Streamlit app UI

---

## 🗂 Folder Structure

```
resume_parser_job_matcher/
├── app/
│ └── app.py ← Streamlit app
├── scripts/ ← Logic modules
│ ├── parse_resume.py
│ ├── job_matcher.py
│ └── text_cleaner.py
├── data/ ← Sample resumes and JDs (gitignored)
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
├── screenshots/
  └── app_ui.png 
```


---

## 🧪 Sample Use

- Upload `resume_ml.docx` and `jd_ml_engineer.docx`
- See candidate info, similarity score, and matched keywords
- Click **Download CSV** for your result

---

## 🛠 Technologies Used

- Python
- Streamlit
- Sentence-Transformers (BERT)
- scikit-learn (TF-IDF, cosine)
- python-docx
- pandas

---

## 📦 Setup Instructions

1. Clone this repo
2. Create virtual environment and install requirements:

```bash
pip install -r requirements.txt
```

---

## 🙌 Acknowledgements

- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)

---

## Run the app

```bash
streamlit run app/app.py
```
---

## 🌐 Live Demo

[![Open in Streamlit](https://resume-parser-job-matcher-ml-nlp.streamlit.app/)

---

## License

This project is licensed under a custom license for **personal and educational use only**.

- ✅ You may use, modify, and share this code for learning and personal projects.
- ❌ Commercial use, resale, or offering this code as part of a paid product/service is **not allowed** without the author's permission.

To request commercial use rights, contact: hpriyavtva2001@gmail.com

---

## 🙋‍♀️ Author

Vyamsani T V A Haripriya  
Data Analyst | Python & ML Enthusiast

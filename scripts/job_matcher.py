from parse_resume import extract_text_from_docx
from text_cleaner import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# Load a small but powerful model
model = SentenceTransformer('all-MiniLM-L6-v2') #load globally


def get_match_score(resume_path, jd_path):
    resume_raw = extract_text_from_docx(resume_path)
    jd_raw = extract_text_from_docx(jd_path)
    resume_cleaned = clean_text(resume_raw)
    jd_cleaned = clean_text(jd_raw)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_cleaned, jd_cleaned])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity * 100, 2)


def get_bert_similarity(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
    return round(similarity * 100, 2)


def extract_top_keywords(text, top_n=10):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()



# scripts/text_cleaner.py

import re
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text):
    """
    Cleans text by:
    - Lowercasing
    - Removing punctuation
    - Removing stopwords
    """
    text = text.lower()
    text = re.sub(r"\n", " ", text)  # Remove line breaks
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)  # Remove punctuation
    tokens = text.split()
    tokens = [word for word in tokens if word not in ENGLISH_STOP_WORDS]
    return " ".join(tokens)

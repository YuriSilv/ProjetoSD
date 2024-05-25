import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from unidecode import unidecode

nltk.download('stopwords')

def clean_text(text):
    text_lower = text.lower()
    text_no_link = re.sub(r'http\S+|www\S+|https\S+', '', text_lower, flags=re.MULTILINE)
    text_no_punct = re.sub(r'[^\w\s]', '', text_no_link)
    text_no_accent = unidecode(text_no_punct)
    text_no_double_space = re.sub(r'\s+', ' ', text_no_accent).strip()
    
    stop_words = set(stopwords.words('portuguese'))
    text_clean = ' '.join([word for word in text_no_double_space.split() if word not in stop_words])
    
    return text_clean
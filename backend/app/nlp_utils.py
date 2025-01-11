from textblob import TextBlob
import spacy
from sklearn.cluster import KMeans
import numpy as np

nlp = spacy.load("en_core_web_sm")


def analyze_sentiment(text):
    blob = TextBlob(text)
    return "Positive" if blob.sentiment.polarity > 0 else "Negative"


def extract_tags(text):
    doc = nlp(text)
    tags = [ent.text for ent in doc.ents]
    return tags


def generate_clusters(comments, n_clusters=5):
    embeddings = np.array([nlp(comment).vector for comment in comments])
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_ids = kmeans.fit_predict(embeddings)
    return cluster_ids

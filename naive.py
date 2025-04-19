import pandas as pd
import re
import numpy as np
from collections import defaultdict

# ---------------------------
# 1. PREPROCESAMIENTO
# ---------------------------

def preprocess(text):
    """Convierte el texto a minúsculas, elimina símbolos y lo tokeniza"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()

# ---------------------------
# 2. CLASIFICADOR NAÏVE BAYES
# ---------------------------

class NaiveBayesClassifier:
    def __init__(self):
        self.class_priors = {}
        self.word_probs = {}
        self.vocab = set()
        self.class_word_counts = {}
        self.class_counts = defaultdict(int)

    def train(self, data):
        total_docs = len(data)
        word_counts = defaultdict(lambda: defaultdict(int))
        
        for label, text in data:
            tokens = preprocess(text)
            self.class_counts[label] += 1
            for token in tokens:
                word_counts[label][token] += 1
                self.vocab.add(token)

        vocab_size = len(self.vocab)

        for label in self.class_counts:
            self.class_priors[label] = self.class_counts[label] / total_docs
            total_words = sum(word_counts[label].values())
            self.class_word_counts[label] = total_words

            self.word_probs[label] = {}
            for word in self.vocab:
                self.word_probs[label][word] = (
                    word_counts[label][word] + 1
                ) / (total_words + vocab_size)

    def predict(self, text):
        tokens = preprocess(text)
        scores = {}
        for label in self.class_priors:
            score = np.log(self.class_priors[label])
            for token in tokens:
                if token in self.vocab:
                    prob = self.word_probs[label].get(
                        token, 1 / (self.class_word_counts[label] + len(self.vocab))
                    )
                    score += np.log(prob)
            scores[label] = score
        return max(scores, key=scores.get)

# ---------------------------
# 3. CARGA Y ENTRENAMIENTO
# ---------------------------

# Carga tu archivo CSV
df = pd.read_csv("twitter_training.csv", header=None)

# Columnas relevantes: sentimiento y texto
df = df[[2, 3]]
df.columns = ["label", "text"]
df = df.dropna(subset=["text"])
df["text"] = df["text"].astype(str)
df["label"] = df["label"].str.lower()

# Opcional: Filtrar solo Positive, Negative, Neutral
allowed = ["positive", "negative", "neutral"]
df = df[df["label"].isin(allowed)]

# Entrenar
model = NaiveBayesClassifier()
model.train(df.values)

# ---------------------------
# 4. PRUEBA DEL MODELO
# ---------------------------

# --- Predecir desde otra parte del programa ---
def predict_from_text(text):
    return model.predict(text)

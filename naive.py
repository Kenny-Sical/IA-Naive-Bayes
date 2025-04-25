import pandas as pd
import re
import numpy as np
import pickle
import os
from collections import defaultdict, Counter
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

MODEL_FILE = "modelo_naive.pkl"

def preprocess(text):
    "Limpieza de datos y tokenización"
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()


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


## Entrena y guarda solo si no existe el modelo
if not os.path.exists(MODEL_FILE):
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

    #Entrenar
    model = NaiveBayesClassifier()
    model.train(df.values)
    #Guardar
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)


# Cargar una vez al importar el archivo
with open(MODEL_FILE, "rb") as f:
    modelo_cargado = pickle.load(f)

def predict_from_text(text):
    return modelo_cargado.predict(text)


def evaluar_modelo():
    """Evalúa el modelo en todo el conjunto de entrenamiento."""
    df = pd.read_csv("twitter_training.csv", header=None)
    df = df[[2, 3]]
    df.columns = ["label", "text"]
    df = df.dropna(subset=["text"])
    df["text"] = df["text"].astype(str)
    df["label"] = df["label"].str.lower()

    allowed = ["positive", "negative", "neutral"]
    df = df[df["label"].isin(allowed)]

    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)

    y_true = df["label"].tolist()
    y_pred = [model.predict(text) for text in df["text"]]

    reporte = classification_report(y_true, y_pred, digits=3)
    return reporte
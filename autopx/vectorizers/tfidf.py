from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDF:
    """
    Wrapper for TfidfVectorizer.
    """
    def __init__(self, **kwargs):
        self.vectorizer = TfidfVectorizer(**kwargs)
        
    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

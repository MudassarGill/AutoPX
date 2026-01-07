from sklearn.feature_extraction.text import CountVectorizer

class Count:
    """
    Wrapper for CountVectorizer.
    """
    def __init__(self, **kwargs):
        self.vectorizer = CountVectorizer(**kwargs)
        
    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

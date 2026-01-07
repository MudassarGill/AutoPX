# autopx/preprocessing/tokenizer.py

import re
from autopx.utils.constants import Language

class Tokenizer:
    """
    Handles tokenization of text based on language and noise level.
    """

    def __init__(self):
        pass

    def tokenize(self, text, language):
        """
        Tokenize the text based on language and script type.
        """
        if not text:
            return []

        if language == Language.ENGLISH:
            # Simple word-level tokenization for English
            tokens = re.findall(r'\b\w+\b', text.lower())
        elif language == Language.URDU:
            # Urdu tokenization: split by spaces, keep punctuation
            tokens = [t for t in text.split() if t.strip()]
        elif language == Language.ROMAN_URDU:
            # Roman Urdu: use character n-grams for noisy text
            tokens = self._char_ngrams(text.lower(), n=3)
        else:
            # Fallback: split by spaces
            tokens = text.split()

        return tokens

    def _char_ngrams(self, text, n=3):
        """
        Create character n-grams from a string.
        """
        text = re.sub(r'\s+', ' ', text)  # normalize spaces
        text = text.strip()
        ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
        return ngrams

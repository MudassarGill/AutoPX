# autopx/core/data_analysis.py

import re
from autopx.utils.constants import Language

class DataAnalyzer:
    """
    Analyzes raw input text to understand structure, length, emojis, and language patterns.
    """

    def analyze(self, texts):
        """
        Analyze the input texts.
        Returns a dictionary with:
            - language: detected language
            - avg_length: average word count
            - has_emojis: True if emojis detected
            - dataset_size: number of texts
        """
        if not texts:
            return {
                'language': Language.UNKNOWN,
                'avg_length': 0,
                'has_emojis': False,
                'dataset_size': 0
            }
        
        avg_len = sum(len(t.split()) for t in texts) / len(texts)

        # Simple Emoji detection regex
        emoji_pattern = re.compile("[\U00010000-\U0010FFFF]", flags=re.UNICODE)
        has_emojis = any(emoji_pattern.search(t) for t in texts[:100])  # Check first 100 texts for speed

        language = self._detect_language(texts)

        return {
            'language': language,
            'avg_length': avg_len,
            'has_emojis': has_emojis,
            'dataset_size': len(texts)
        }

    def _detect_language(self, texts):
        """
        Detects English, Urdu, or Roman Urdu using simple heuristics.
        """
        sample_text = " ".join(texts[:5])  # Sample first few texts

        # Urdu Unicode Range: 0600–06FF
        if re.search(r'[\u0600-\u06FF]', sample_text):
            return Language.URDU

        # Roman Urdu heuristic (common words)
        roman_ur_keywords = ['hai', 'main', 'kya', 'kaise', 'bhi', 'tha', 'thi']
        words = set(re.findall(r'\b\w+\b', sample_text.lower()))
        if len(words.intersection(roman_ur_keywords)) > 0:
            return Language.ROMAN_URDU

        # Default to English
        return Language.ENGLISH

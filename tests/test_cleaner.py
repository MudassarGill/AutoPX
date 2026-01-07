# tests/test_cleaner.py

import unittest
from autopx.preprocessing.cleaner import Cleaner
from autopx.utils.constants import TaskType, Language

class TestCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = Cleaner()
    
    def test_clean_english_sentiment(self):
        text = "I love this! 😄 Visit http://example.com"
        cleaned = self.cleaner.clean(text, TaskType.SENTIMENT, Language.ENGLISH)
        self.assertIn("love", cleaned)
        # In current implementation, _remove_special_characters_preserve_emojis might handle space differently
        # Let's check for the emoji itself
        self.assertIn("😄", cleaned)
        self.assertNotIn("http://example.com", cleaned)
    
    def test_clean_urdu_text(self):
        text = "یہ ایک بہترین کتاب ہے!"
        cleaned = self.cleaner.clean(text, TaskType.SENTIMENT, Language.URDU)
        self.assertIn("بہترین", cleaned)
        self.assertNotIn("!", cleaned)
    
    def test_clean_roman_urdu(self):
        text = "Main bohat khush hoon! 😄"
        cleaned = self.cleaner.clean(text, TaskType.CHATBOT, Language.ROMAN_URDU)
        self.assertIn("khush", cleaned)
        self.assertIn("😄", cleaned)

if __name__ == "__main__":
    unittest.main()

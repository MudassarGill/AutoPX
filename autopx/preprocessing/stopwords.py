# autopx/preprocessing/stopwords.py

from autopx.utils.constants import Language, TaskType

class StopwordHandler:
    """
    Handles stopword removal/preservation based on task and language.
    """

    # Basic English stopwords (extendable)
    ENGLISH_STOPWORDS = {
        "the", "a", "an", "and", "or", "but", "if", "in", "on", "with", "for", "of", "at", "by"
    }

    # Basic Urdu stopwords (extendable)
    URDU_STOPWORDS = {
        "ہے", "کا", "کی", "کے", "میں", "کو", "سے", "یہ", "وہ"
    }

    # Basic Roman Urdu stopwords (extendable)
    ROMAN_URDU_STOPWORDS = {
        "hai", "ka", "ki", "ke", "main", "ko", "se", "ye", "wo"
    }

    def __init__(self):
        pass

    def remove_stopwords(self, text, task, language):
        """
        Remove stopwords based on language and task.
        For sentiment analysis and chatbot tasks, stopwords may be preserved.
        """
        if not text:
            return ""

        words = text.split()

        # Decide whether to remove stopwords
        remove = True
        if task in [TaskType.SENTIMENT, TaskType.CHATBOT]:
            remove = False

        if not remove:
            return text

        if language == Language.ENGLISH:
            stopwords = self.ENGLISH_STOPWORDS
        elif language == Language.URDU:
            stopwords = self.URDU_STOPWORDS
        elif language == Language.ROMAN_URDU:
            stopwords = self.ROMAN_URDU_STOPWORDS
        else:
            stopwords = set()

        filtered = [w for w in words if w.lower() not in stopwords]
        return " ".join(filtered)

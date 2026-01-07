# autopx/core/decision_engine.py

from autopx.utils.constants import TaskType, ModelType, VectorizationType, Language

class DecisionEngine:
    """
    Selects the most suitable NLP task and vectorization strategy
    based on text analysis.
    """

    def infer_task(self, texts, analysis_report):
        """
        Infers the NLP task based on text characteristics.
        Returns one of: TaskType.SENTIMENT, TaskType.TOPIC_MODELING, TaskType.CHATBOT
        """
        avg_len = analysis_report.get('avg_length', 0)
        has_emojis = analysis_report.get('has_emojis', False)

        # Heuristic 1: Short text + emojis -> Sentiment Analysis
        if avg_len < 30 and has_emojis:
            return TaskType.SENTIMENT

        # Heuristic 2: Long text -> Topic Modeling
        if avg_len > 100:
            return TaskType.TOPIC_MODELING

        # Default fallback -> Chatbot/Dialogue
        return TaskType.CHATBOT

    def select_vectorization(self, task, model_type, dataset_size):
        """
        Selects the vectorization strategy based on task, model type, and dataset size.
        Returns one of: VectorizationType.TFIDF, COUNT, EMBEDDINGS, SEQUENCE
        """
        # Deep learning or transformer models → sequence-based vectors
        if model_type in [ModelType.DL, ModelType.TRANSFORMERS]:
            return VectorizationType.SEQUENCE

        # Topic modeling → TFIDF
        if task == TaskType.TOPIC_MODELING:
            return VectorizationType.TFIDF

        # Small datasets → CountVectorizer
        if dataset_size < 1000:
            return VectorizationType.COUNT

        # Default fallback → TFIDF
        return VectorizationType.TFIDF

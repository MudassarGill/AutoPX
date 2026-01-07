from autopx.core.data_analysis import DataAnalyzer
from autopx.core.decision_engine import DecisionEngine
from autopx.preprocessing.cleaner import Cleaner
from autopx.utils.constants import TaskType, ModelType, VectorizationType
from autopx.utils.logger import Logger
from autopx.vectorizers.tfidf import TFIDF
from autopx.vectorizers.count import Count
from autopx.vectorizers.embeddings import Embeddings
from autopx.reports.report_builder import ReportBuilder

class AutoPX:
    """
    Main AutoPX pipeline class.
    Orchestrates the entire preprocessing workflow.
    """
    def __init__(self, task=None, model_type=ModelType.ML):
        self.task = task
        self.model_type = model_type
        
        self.analyzer = DataAnalyzer()
        self.decision_engine = DecisionEngine()
        self.cleaner = Cleaner()
        self.logger = Logger()
        self.report_builder = ReportBuilder()
        
        self.last_report = {}
        
    def fit_transform(self, texts):
        """
        Main method to preprocess data and return model-ready vectors.
        """
        self.logger.info("Starting AutoPX pipeline...")

        # 1️⃣ Analyze Data (Language, Stats)
        analysis_report = self.analyzer.analyze(texts)
        self.logger.info(f"Analysis complete. Detected Language: {analysis_report['language']}")

        # 2️⃣ Infer Task (if not provided)
        current_task = self.task
        if not current_task:
            current_task = self.decision_engine.infer_task(texts, analysis_report)
            self.logger.info(f"Task inferred: {current_task}")

        # 3️⃣ Clean Text
        cleaned_texts = []
        for t in texts:
            cleaned_texts.append(self.cleaner.clean(t, current_task, analysis_report['language']))
        self.logger.info("Text cleaning complete.")

        # 4️⃣ Select Vectorization
        vec_strategy = self.decision_engine.select_vectorization(
            current_task,
            self.model_type,
            analysis_report['dataset_size']
        )
        self.logger.info(f"Vectorization strategy selected: {vec_strategy}")

        # 5️⃣ Store Report Info
        self.last_report = {
            'analysis': analysis_report,
            'task': current_task,
            'vectorization': vec_strategy,
            'cleaned_texts': cleaned_texts
        }

        # 6️⃣ Apply Vectorization
        if vec_strategy == VectorizationType.TFIDF:
            vectors = TFIDF().fit_transform(cleaned_texts)
        elif vec_strategy == VectorizationType.COUNT:
            vectors = Count().fit_transform(cleaned_texts)
        elif vec_strategy == VectorizationType.EMBEDDINGS:
            vectors = Embeddings().fit_transform(cleaned_texts)
        else:
            self.logger.info("Unknown vectorization strategy. Defaulting to TFIDF.")
            vectors = TFIDF().fit_transform(cleaned_texts)

        self.logger.info("Vectorization complete.")
        return vectors

    def report(self, format="pdf"):
        """
        Generates an explainable report of the last preprocessing run.
        """
        if not self.last_report:
            self.logger.info("No report available. Run fit_transform() first.")
            return None
        self.logger.info(f"Generating {format} report...")
        return self.report_builder.generate(self.last_report, format=format)

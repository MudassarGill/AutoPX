# verify_structure.py

"""
Script to verify AutoPX folder structure.
"""

import os

# Define required structure
required_structure = [
    "autopx/__init__.py",
    "autopx/core/autopx.py",
    "autopx/core/data_analysis.py",
    "autopx/core/decision_engine.py",
    "autopx/preprocessing/cleaner.py",
    "autopx/preprocessing/sequence_handler.py",
    "autopx/preprocessing/stopwords.py",
    "autopx/preprocessing/tokenizer.py",
    "autopx/fallback/fallback_manager.py",
    "autopx/fallback/fallback_rules.py",
    "autopx/reports/report_builder.py",
    "autopx/utils/constants.py",
    "autopx/utils/helpers.py",
    "autopx/utils/logger.py",
    "autopx/vectorizers/count.py",
    "autopx/vectorizers/embeddings.py",
    "autopx/vectorizers/tfidf.py",
]

def verify_structure(base_path="."):
    missing_files = []
    for f in required_structure:
        path = os.path.join(base_path, f)
        if not os.path.exists(path):
            missing_files.append(f)

    if missing_files:
        print(" Missing files/folders:")
        for f in missing_files:
            print(f"   - {f}")
    else:
        print(" All required files and folders are present!")

if __name__ == "__main__":
    verify_structure()

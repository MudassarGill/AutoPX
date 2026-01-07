# verify_install.py

"""
Script to verify that AutoPX can be imported and basic functionality works.
"""

from autopx import AutoPX, TaskType, ModelType

def test_autopx_import():
    try:
        # Create a dummy AutoPX instance
        autopx_instance = AutoPX(task=TaskType.SENTIMENT, model_type=ModelType.ML)
        print("✅ AutoPX imported and instance created successfully!")
    except Exception as e:
        print("❌ AutoPX import failed!")
        print(e)

if __name__ == "__main__":
    test_autopx_import()

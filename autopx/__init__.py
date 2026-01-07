# autopx/__init__.py

"""
AutoPX: Automatic Preprocessing with eXplainability

Main package initializer for the AutoPX library.
This file exposes the core AutoPX class for external usage.
"""

from autopx.core.autopx import AutoPX
from autopx.utils.constants import TaskType, ModelType, VectorizationType, Language

# Expose these for easy import:
__all__ = [
    "AutoPX",
    "TaskType",
    "ModelType",
    "VectorizationType",
    "Language"
]

"""
crimedatasets
A Python package providing crime-related datasets in CSV format from Kaggle sources.
"""

__version__ = "0.1.0"

from .core import load_dataset, list_datasets
from .datasets import DATASETS

__all__ = [
    "load_dataset",
    "list_datasets",
    "DATASETS",
    "__version__",
]
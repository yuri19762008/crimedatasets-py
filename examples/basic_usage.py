"""
Basic usage example for crimedatasets

Run:
    python basic_usage.py
"""

import crimedatasets as crd

print("=== crimedatasets: Basic Usage Example ===\n")

# Load a dataset
print("Loading 'us_mass_shootings' dataset...")
shootings = crd.load_dataset("us_mass_shootings")

# Show basic information
print("\nFirst 5 rows:")
print(shootings.head())

print("\nDataset shape:")
print(shootings.shape)

print("\nColumn names:")
print(list(shootings.columns))

# Load another dataset
print("\nLoading 'corruption_index_2012_2022' dataset...")
corruption = crd.load_dataset("corruption_index_2012_2022")

print("\nFirst 5 rows:")
print(corruption.head())

print("\nDone.")

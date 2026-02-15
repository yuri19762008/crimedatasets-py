# crimedatasets – Examples

This page provides practical examples of using `crimedatasets` for data analysis and exploration.

## Basic Examples

### Example 1: Loading and Exploring a Dataset

Learn how to load a dataset and perform basic exploration.

```python
import crimedatasets as crd

# Load the Mass Shootings in the USA dataset
shootings = crd.load_dataset("us_mass_shootings")

# Display first few rows
print(shootings.head())

# Check dataset shape
print(f"\nDataset shape: {shootings.shape}")

# View column names
print(f"\nColumns: {list(shootings.columns)}")

# Get summary statistics
print("\nSummary statistics:")
print(shootings.describe())

# Check for missing values
print("\nMissing values:")
print(shootings.isnull().sum())

```

### Example 2: Maryland Crime Data Analysis

Explore crime trends across Maryland counties over time.

```python
import crimedatasets as crd

# Load Maryland crime data
md_crime = crd.load_dataset("maryland_crime_counties")

# Display first few rows
print(md_crime.head())

# Check dataset shape
print(f"\nDataset shape: {md_crime.shape}")

# View column names
print(f"\nColumns: {list(md_crime.columns)}")

# Filter data for a specific county
allegany = md_crime[md_crime['JURISDICTION'] == 'Allegany County']
print("\nAllegany County - First 10 years:")
print(allegany[['YEAR', 'POPULATION', 'MURDER', 'RAPE', 'ROBBERY']].head(10))

```
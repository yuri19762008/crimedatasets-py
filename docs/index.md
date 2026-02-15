# crimedatasets Documentation

## Welcome

The `crimedatasets` package provides a comprehensive collection of crime-related datasets from around the world. It includes extensive data on topics such as **mass shootings, hate crimes, incarceration statistics, serial killers, corruption indexes, law enforcement data, criminal justice metrics, drug overdoses, and prison facilities**.

The package contains historical crime statistics, mass shooting incidents, hate crime records, death row inmate information, serial killer profiles, drug overdose mortality rates, presidential pardons, juvenile arrest data and much more.

### Philosophy

The author's vision is to create **specialized dataset packages** focused on specific themes and topics. Instead of searching through multiple generic data packages to find relevant datasets, users can go directly to a thematic package where all datasets are carefully curated around a particular subject.

In the case of `crimedatasets`, every dataset is **exclusively focused on crime, criminal justice, public safety, and law enforcement**, making it the go-to resource for researchers, data scientists, criminologists, law enforcement agencies, policy analysts, sociologists, and students working in the criminology, criminal justice, and public safety fields.

### Cross-Platform Ecosystem

`crimedatasets` has a sibling package in the R ecosystem called **<a href="https://lightbluetitan.github.io/crimedatasets/" target="_blank" rel="noopener">crimedatasets</a>**, maintaining consistency across programming languages and ensuring that users can work with the same high-quality datasets whether they prefer Python or R.

This cross-platform approach reflects our commitment to making specialized datasets accessible to the widest possible audience, regardless of their preferred data analysis environment.

## Getting Started

### Installation

#### From PyPI (Recommended)

The easiest way to install `crimedatasets` is directly from PyPI:
```bash
pip install crimedatasets
```

#### From GitHub (Latest Development Version)

To get the latest development version with the newest features and bug fixes:
```bash
pip install git+https://github.com/lightbluetitan/crimedatasets-py
```

### Quick Start Tutorial

#### 1. Import the Package
```python
import crimedatasets as crd
```

#### 2. List Available Datasets

See all datasets included in the package:
```python
# Get list of all datasets
datasets = crd.list_datasets()
print(datasets)
```

#### 3. Load a Dataset

Load any dataset as a pandas DataFrame:
```python
# Load us_mass_shootings
df = crd.load_dataset('us_mass_shootings')

# Display first rows
print(df.head())

# Check dataset dimensions
print(f"Shape: {df.shape}")
```


### Basic Concepts

#### Dataset Naming Convention

All dataset names in `crimedatasets` follow a consistent naming pattern:

- Lowercase with underscores: `us_mass_shootings`
- Descriptive names that reflect content
- Some include time periods: `corruption_index_2012_2022`, `presidential_pardons_1967_2017`


#### Some  Datasets available at `crimedatasets`

Every dataset is **exclusively focused on crime, criminal justice, public safety, and law enforcement**:

- **maryland_crime_counties**: Maryland Crime Data by County 1975-2020.
- **texas_deathrow**: Texas death row inmates executed from 1976 to 2018.
- **nypd_hate_crimes**: NYPD Hate Crime Dataset.
- **crime_incarceration_by_state**: A dataset of crime and prisoner figures by state from 2001-2017.


#### Data Licenses

All datasets maintain their original open-source licenses:

- Most datasets use **CC0: Public Domain** (free for any use)
- Some use **MIT License** or **Apache 2.0**
- The `crimedatasets` package itself is licensed under **MIT**
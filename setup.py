from setuptools import setup, find_packages
import os

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="crimedatasets",
    version="0.1.0",
    author="Renzo Caceres Rossi",
    author_email="arenzocaceresrossi@gmail.com",
    description=(
        "A curated collection of crime-related datasets for data analysis, "
        "criminology research, and education. Includes international crime statistics, "
        "incarceration data, mass shootings, hate crimes, and more from Kaggle sources."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lightbluetitan/crimedatasets-py",
    project_urls={
        "Bug Tracker": "https://github.com/lightbluetitan/crimedatasets-py/issues",
        "Documentation": "https://github.com/lightbluetitan/crimedatasets-py",
        "Source Code": "https://github.com/lightbluetitan/crimedatasets-py",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "crimedatasets": [
            "data/*.csv",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        
        # Topics
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Sociology",  
        "Topic :: Database",
        
        # Versiones de Python
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        
        # Sistema Operativo
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords=(
        "datasets, crime, criminology, criminal justice, crime statistics, "
        "law enforcement, incarceration, hate crimes, mass shootings, prisons, "
        "data analysis, data science, research, sociology, international, kaggle"
    ),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    license="MIT",
    zip_safe=False,
)
# CleanData4ML

Data preprocessing pipeline for Machine Learning

## Description

This project provides a complete pipeline for data preprocessing before its use in Machine Learning models. It includes functionality for:

- Loading data from different formats (CSV, space-delimited)
- Handling missing values (median imputation for numerical, 'UNKNOWN' for categorical)
- Transforming categorical variables (Label Encoding, One-Hot Encoding)
- Scaling numerical variables (StandardScaler)
- Splitting into training and test sets (80/20 by default)
- Dataset-specific configuration management

## Project Structure
CleanData4ML/
│
├── data/ # Data directories
│ ├── raw/ # Original raw datasets
│ │ ├── churn-bigml-20.csv
│ │ ├── churn-bigml-80.csv
│ │ ├── house_prediction_dataset.csv
│ │ ├── iris_dataset.csv
│ │ ├── sentiment_dataset.csv
│ │ └── stock_prices_dataset.csv
│ │
│ └── processed/ # Processed datasets (train/test splits)
│ ├── churn_20/
│ ├── churn_80/
│ ├── housing/
│ ├── iris/
│ ├── sentiment/
│ └── stocks/
│
├── src/ # Source code
│ ├── preprocessing/ # Data processing modules
│ │ ├── clean_data.py # Missing value handling
│ │ ├── load_data.py # Data loading utilities
│ │ ├── split_data.py # Train/test splitting
│ │ ├── transform.py # Feature transformations
│ │ └── init.py
│ │
│ └── config.py # Dataset configurations
│
├── main.py # Main execution script
├── README.md # This documentation
├── LICENSE # MIT License
└── .gitignore

## Supported Datasets

The pipeline comes pre-configured for these datasets:

1. **Iris** (Classification)
   - Target: Species classification
   - Special handling: Keeps species as string

2. **Sentiment Analysis** (Text/NLP)
   - Drops metadata columns
   - Handles platform categorical data

3. **Housing Prices** (Regression)
   - Space-delimited format
   - MEDV as target variable

4. **Stock Prices** (Time-series)
   - Maintains symbol as string identifier
   - Numerical price/volume features

5. **Churn Prediction** (Binary Classification)
   - Two versions (20% and 80% samples)
   - Special handling for State (One-Hot Encoding)

## Configuration

All dataset parameters are centrally configured in `src/config.py` including:
- File paths
- Column types (numerical/categorical)
- Target variables
- Special processing instructions
- Encoding methods per feature

## Requirements

- Python 3.8+
- Dependencies:
  - pandas
  - scikit-learn

Install requirements:
```bash
pip install -r requirements.txt

Usage

Process all datasets:
python main.py

Process specific dataset:
from src.preprocessing.load_data import load_dataset
from main import process_dataset
process_dataset("iris")  
#  UAE Real Estate Analytics & Price Prediction

### What is happening in the UAE real-estate market — and can property prices be predicted from historical transactions?

An end-to-end **data analytics and machine learning project** using real-world public property data from **Dubai and Ajman**.

The project starts with raw real-estate records, transforms them into analysis-ready data, explores market trends, and builds machine-learning models to predict Dubai residential sale prices.

##  From Raw Data to Insights 📊

- **898K+** raw Dubai property records analyzed
- **550K+** qualifying residential sales prepared for analysis
- Real transactions covering different property types and transaction categories
- Dubai and Ajman market trends compared from **2019–2026**
- Price, location, property type, size, and sales activity explored

The raw Dubai data was not reduced because the remaining records were simply "bad." Transactions such as **mortgages, gifts, commercial properties, and land** were excluded from the ML dataset to focus specifically on **residential Unit & Villa sales**.

## What Does the Analysis Show?

-  How property prices and sales activity change over time
-  Which Dubai areas have higher property values
-  Differences between property types and bedroom categories
-  How property size relates to sale price
- 🇦🇪 How Dubai and Ajman market activity has changed since 2019
-  How prediction performance changes across normal and luxury properties

##  Machine Learning

Three regression models were evaluated:

**Linear Regression** · **HistGradientBoosting Regressor** · **Log-HistGradientBoosting Regressor**

The models use:

`Location` · `Property Type` · `Bedrooms` · `Size` · `Parking` · `Year` · `Quarter`

### Prediction Results

| Model | Within ±20% | Within ±30% |
|---|---:|---:|
| Linear Regression | 41.8% | 57.3% |
| HistGradientBoosting | 50.7% | 72.1% |
| **Log-HistGradientBoosting** | **51.7%** | **74.7%** |

**Log-HistGradientBoosting** achieved the lowest overall MAE of approximately **AED 563K**, with **74.7% of predictions falling within ±30% of the actual sale price**.

Prediction became more difficult for luxury properties, highlighting the complexity and variability of real-world property prices.

## Project

- `03_dubai_cleaning.ipynb` — Raw data → clean residential transactions
- `04_ajman_cleaning.ipynb` — Ajman data preparation
- `05_exploratory_analysis.ipynb` — Market trends & Dubai–Ajman analysis
- `06_dubai_price_model.ipynb` — Machine learning & evaluation

##  Tech Stack

**Python · Pandas · NumPy · Matplotlib · scikit-learn · Jupyter · Git · GitHub**

> **Data Note:** This project uses real-world public real-estate data. Raw and processed datasets are excluded from GitHub due to file size and data-distribution considerations.
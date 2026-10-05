#  UAE Real Estate Analytics & Price Prediction 🏙️

### What is happening in the UAE real-estate market and can property prices be predicted from historical transactions?

An end-to-end **data analytics and machine learning project** using real-world public property data from **Dubai and Ajman**.

The project transforms raw real-estate records into market insights and uses machine learning to predict Dubai residential sale prices.

##  From Raw Data to Insights 📊

- **898K+** raw Dubai property records analyzed
- **550K+** qualifying residential sales prepared for analysis
- Dubai and Ajman market trends compared from **2019–2026**
- Price, location, property type, size, and sales activity explored

Transactions such as **mortgages, gifts, commercial properties, and land** were excluded from the ML dataset to focus specifically on **residential Unit & Villa sales**.

##  Market Analysis

###  Dubai Property Price Trend

Dubai residential median sale prices increased strongly after 2020, reaching their highest levels around 2022–2023 before showing some moderation.

![Dubai Residential Price Trend](images/dubai_price_trend.png)

###  Highest-Priced Dubai Areas

The analysis compares median residential sale prices across Dubai areas with sufficient transaction activity, highlighting major differences between locations.

![Top Dubai Areas](images/dubai_top_areas.png)

###  Dubai vs Ajman Sales Activity

Because Dubai and Ajman datasets have different structures, sales activity was normalized using **2019 = 100** to compare how both markets changed over time.

![Dubai vs Ajman Sales Activity](images/dubai_ajman_activity.png)

###  Dubai vs Ajman Property Value Trend

Normalized property values show how residential market values in both emirates evolved relative to their 2019 levels.

![Dubai vs Ajman Sale Value Trend](images/dubai_ajman_value.png)

##  Machine Learning

Three regression models were evaluated:

**Linear Regression** · **HistGradientBoosting Regressor** · **Log-HistGradientBoosting Regressor**

Models use:

`Location` · `Property Type` · `Bedrooms` · `Size` · `Parking` · `Year` · `Quarter`

| Model | MAE (AED) | R² |
|---|---:|---:|
| Linear Regression | 711,818 | **0.644** |
| HistGradientBoosting | 579,150 | 0.409 |
| **Log-HistGradientBoosting** | **562,645** | 0.407 |

The Log-HistGradientBoosting model achieved the **lowest overall MAE**, while Linear Regression achieved the **highest R²**.

###  Actual vs Predicted Prices

Predictions follow actual prices more closely for lower and mid-priced properties. Errors increase for high-value properties, with the model tending to underestimate some luxury transactions.

![Actual vs Predicted Property Prices](images/actual_vs_predicted.png)

## Project

- `03_dubai_cleaning.ipynb` — Raw Dubai data → clean residential transactions
- `04_ajman_cleaning.ipynb` — Ajman data preparation
- `05_exploratory_analysis.ipynb` — Market trends & Dubai–Ajman comparison
- `06_dubai_price_model.ipynb` — Machine learning & model evaluation

##  Tech Stack

**Python · Pandas · NumPy · Matplotlib · scikit-learn · Jupyter · Git · GitHub**

> **Data Note:** This project uses real-world public real-estate data. Raw and processed datasets are excluded from GitHub due to file size and data-distribution considerations.
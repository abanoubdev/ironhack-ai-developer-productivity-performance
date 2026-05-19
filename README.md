# Predictive Task Duration Analysis

A machine learning project designed to transition software development estimation from subjective "gut feeling" to data-driven forecasting. This repository contains a full pipeline for predicting task completion times based on developer activity, workflow tools, and human-centric factors.

## 🚀 Project Overview
Estimating task duration is a recurring challenge in Agile environments. This project analyzes developer logs to identify the most significant predictors of task length and compares multiple regression models to find the most robust predictive engine.

## 📊 Dataset Features
The model utilizes 9 core features categorized into three dimensions:
* **Technical Activity:** `Hours_Coding`, `Lines_of_Code`, `Bugs_Found`, `Commits`.
* **Workflow Tools:** `AI_Usage_Hours`.
* **Human Factors:** `Sleep_Hours`, `Cognitive_Load`, `Coffee_Intake`, `Stress_Level`.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** * `Pandas` & `NumPy` for data manipulation.
    * `Scikit-Learn` for preprocessing and modeling.
    * `Matplotlib` & `Seaborn` for statistical visualization.

## ⚙️ Implementation Pipeline

### 1. Data Preprocessing

* **Standardization:** Applied `StandardScaler` to normalize features with varying units (e.g., hundreds of lines of code vs. single-digit coffee cups) to ensure equal mathematical weighting.
* **Validation Strategy:** Implemented an 80/20 Train-Test split to verify model performance on unseen data and ensure generalizability.

### 2. Modeling Strategy
We followed an iterative "Model Evolution" approach to test different algorithmic assumptions:
1.  **Baseline:** **Linear Regression** (Ordinary Least Squares) to establish a performance benchmark.
2.  **Ensemble Learning:** **Random Forest Regressor** (100 estimators) to test for non-linear interactions and feature dependencies.
3.  **Sequential Optimization:** **Gradient Boosting Regressor** (GBR) to minimize residual errors through iterative learning.

### 3. Feature Engineering
Advanced metrics were created to capture workflow efficiency beyond raw activity:
* **AI-to-Manual Ratio:** Measuring the relative impact of AI assistance on output.
* **Total Active Hours:** A combined metric of manual coding and AI-assisted hours.

## 📈 Results & Performance Comparison

| Model | Mean Absolute Error (MAE) | R-squared ($R^2$) |
| :--- | :--- | :--- |
| **Linear Regression** | **3.00h** | **0.5677** |
| Random Forest | 3.13h | 0.5337 |
| Gradient Boosting | 3.17h | 0.5186 |

**Key Finding:** The baseline Linear Regression model outperformed complex ensembles. This indicates a strong, direct proportionality between input features and task duration for this specific dataset.

## 💡 Key Insights
* **AI Integration:** Empirical evidence shows that **AI Usage Hours** consistently correlate with reduced task duration, justifying further investment in AI-assisted workflows.
* **Developer Well-being:** Factors like **Sleep** and **Stress Levels** are measurable predictors of delivery speed; integrating these into capacity planning can improve sprint reliability.
* **Predictive Drivers:** While `Hours_Coding` remains the primary driver, `AI_Usage` and `Cognitive_Load` emerged as critical secondary signals for accuracy.

## Presentation
https://canva.link/o1b2elhob1sj9ev

## 📂 Repository Structure
```text
├── clean_data_notebook.ipynb  # Main analysis, feature engineering, and modeling
├── README.md                  # Project documentation
└── data/                      # Dataset source files

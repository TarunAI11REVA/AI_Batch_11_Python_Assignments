# Medical Insurance Charges Prediction with Linear Regression
#
# We want to predict how much a person’s medical insurance will cost ("charges")
# based on information like age, BMI, smoking status, region, etc.
#
# This script walks through a complete ML workflow:
# 1) Load the data
# 2) Make sure the data looks sane (no missing values, duplicates)
# 3) Explore patterns in the data (EDA)
# 4) Prepare the data so a machine learning model can understand it
# 5) Train a Linear Regression model
# 6) Evaluate how well it performs
# 7) Interpret which features matter most
# 8) Visualize predictions vs reality
#
# DATA FILE...
# "medical-charges.csv" in the same directory as this script


import pandas as pd
# pandas is our main tool for working with data tables.
# You can think of a pandas DataFrame as a spreadsheet in Python
# where rows are people and columns are features (age, BMI, etc.).

import numpy as np
# NumPy is used for math operations.
# Here we mainly use it for:
# - log transformations (np.log1p)
# - square roots (np.sqrt)

import matplotlib.pyplot as plt
# matplotlib lets us create plots so we can visually understand the data.


# Import machine learning tools from scikit-learn

from sklearn.model_selection import train_test_split
# This function splits our data into:
# - training data (used to teach the model)
# - testing data (used to check how well it learned)

from sklearn.preprocessing import StandardScaler
# StandardScaler rescales numeric features so they:
# - have mean = 0
# - have standard deviation = 1
#
# This prevents features with large values (like BMI)
# from dominating smaller-scale features (like children).

from sklearn.linear_model import LinearRegression
# LinearRegression fits a straight-line relationship:
# charges = b0 + b1*x1 + b2*x2 + ...
#
# The model learns the best coefficients (b’s) from the data.

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# These are the metrics we’ll use to judge performance:
# - MAE  : average absolute error in dollars
# - RMSE : like MAE but penalizes big mistakes more
# - R-square   : how much of the variation in charges we explain


# Load the dataset

df = pd.read_csv("machine-learning-module-3/assignment-1/medical-charges.csv")
# This reads the CSV file and turns it into a DataFrame called df.
# If the file path is wrong, Python will raise a FileNotFoundError.

print("Dataset shape (rows, columns):", df.shape)
# This tells us how many rows (people) and columns (features) we have.
# It’s a quick check that the file loaded correctly.

print("First 5 rows of the dataset:")
print(df.head())
# Seeing the first few rows helps confirm:
# - column names
# - value ranges
# - whether anything looks obviously wrong

print("Dataset structure and data types:")
print(df.info())
# df.info() is very useful:
# - shows which columns are numeric vs categorical
# - shows if any values are missing
# - helps plan preprocessing steps


# Basic data quality checks

print("Missing values per column:")
print(df.isna().sum())
# This counts how many missing values (NaN) appear in each column.
# Missing data can break models or bias results, so we check early.

print("Number of duplicate rows:")
print(df.duplicated().sum())
# Duplicate rows mean the same person appears more than once.
# If duplicates exist, we would usually remove them.

# In most common insurance datasets, there are no missing values
# and no duplicates — but we always check instead of assuming.


# Exploratory Data Analysis (EDA)

# EDA helps us understand:
# - how charges are distributed
# - which features seem related to cost
# - whether transformations might help

# ---- Distribution of insurance charges ----
plt.figure()
plt.hist(df["charges"], bins=30)
# This histogram shows how insurance costs are spread out.
# Typically, most people have moderate costs,
# while a small number have very large costs (right-skewed).

plt.title("Distribution of Medical Insurance Charges")
plt.xlabel("Charges")
plt.ylabel("Number of people")
plt.show()

# ---- Log-transformed charges ----
plt.figure()
plt.hist(np.log1p(df["charges"]), bins=30)
# log(1 + charges) compresses large values and spreads smaller ones.
# This often makes the distribution look more symmetric,
# which linear models tend to handle better.

plt.title("Distribution of log(1 + Charges)")
plt.xlabel("log(1 + charges)")
plt.ylabel("Number of people")
plt.show()

# ---- Age vs Charges ----
plt.figure()
plt.scatter(df["age"], df["charges"], s=10)
# Each dot represents one person.
# We look for patterns: do charges increase with age?

plt.title("Age vs Charges")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.show()

# ---- BMI vs Charges ----
plt.figure()
plt.scatter(df["bmi"], df["charges"], s=10)
# Higher BMI often corresponds to higher medical risk,
# so we expect at least some upward trend here.

plt.title("BMI vs Charges")
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.show()

# ---- Smoking and charges ----
print("Average charges by smoking status:")
print(df.groupby("smoker")["charges"].mean())
# This comparison is usually very revealing:
# smokers tend to have dramatically higher insurance costs.

# ---- Age vs Charges, separated by smoking status ----
for label, color in [("yes", "red"), ("no", "blue")]:
    subset = df[df["smoker"] == label]
    # We split the data into smokers and non-smokers
    # and plot them in different colors.

    plt.scatter(
        subset["age"],
        subset["charges"],
        s=15,
        alpha=0.6,
        color=color,
        label=f"Smoker = {label}"
    )

plt.title("Age vs Charges (Smokers vs Non-Smokers)")
plt.xlabel("Age")
plt.ylabel("Charges")
plt.legend()
plt.show()

# ---- Gender comparison ----
print("\nAverage charges by sex:")
print(df.groupby("sex")["charges"].mean())
# Gender differences usually exist but are much smaller
# than smoking or age effects.

# ---- Region comparison ----
print("\nAverage charges by region:")
print(df.groupby("region")["charges"].mean())
# Region can matter slightly due to healthcare costs,
# but it’s rarely a dominant factor.


# Prepare the data for machine learning

# Machine learning models only understand numbers.
# Columns like "sex", "smoker", and "region" are text,
# so we convert them into numeric indicator variables.

df_encoded = pd.get_dummies(df, drop_first=True)
# One-hot encoding creates 0/1 columns for each category.
# drop_first=True avoids redundancy and multicollinearity.

# Separate input features (X) from the target variable (y)
X = df_encoded.drop("charges", axis=1)
# X contains everything the model uses to make predictions.

y = df_encoded["charges"]
# y is what we are trying to predict.


# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# We train on 80% of the data and test on 20%.
# random_state ensures the same split every time,
# which makes results reproducible.


# Feature scaling

scaler = StandardScaler()
# We fit the scaler ONLY on training data.
# This prevents leaking information from the test set.

X_train_scaled = scaler.fit_transform(X_train)
# The model learns feature means and standard deviations here.

X_test_scaled = scaler.transform(X_test)
# Test data is scaled using the same rules as training data.


# Train the Linear Regression model

model = LinearRegression()
# This creates an empty Linear Regression model.

model.fit(X_train_scaled, y_train)
# The model now learns:
# - one coefficient per feature
# - an intercept term
# by minimizing squared prediction errors.


# Evaluate the model

y_pred = model.predict(X_test_scaled)
# We ask the model to predict charges for people it has never seen.

mae = mean_absolute_error(y_test, y_pred)
# MAE tells us the average absolute dollar error.

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# RMSE penalizes large mistakes more than MAE.

r2 = r2_score(y_test, y_pred)
# R-sqaure tells us how much of the variation in charges we explain.

print("MODEL PERFORMANCE")
print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"Root Mean Squared Error (RMSE): ${rmse:,.2f}")
print(f"R-squared (R-square): {r2:.4f}")


# Interpret the model

# Each feature has a coefficient:
# - positive  => increases predicted charges
# - negative  => decreases predicted charges
#
# Because we scaled the features, coefficient sizes are comparable.

coefficients = pd.Series(model.coef_, index=X.columns)
coefficients = coefficients.sort_values(key=lambda s: s.abs(), ascending=False)

print("Top predictors of medical charges:")
print(coefficients.head(10))


# Actual vs Predicted visualization

plt.figure()
plt.scatter(y_test, y_pred, s=10)
# If predictions were perfect, points would lie on a 45° line.

plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Medical Charges")
plt.show()


# Final takeaway

print("\nCONCLUSION")
print("- Smoking status is usually the strongest driver of insurance cost.")
print("- Age and BMI also play major roles.")
print("- Sex and region tend to have smaller effects.")
print(f"- This linear model explains about {r2*100:.1f}% of the variation in charges.")
print("- It’s a strong baseline, but non-linear models can often do even better.")

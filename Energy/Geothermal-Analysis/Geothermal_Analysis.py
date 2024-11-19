import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
import lightgbm as lgb
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Simulating a geothermal reservoir dataset
np.random.seed(42)

# Generating synthetic data
n_samples = 500
temperature_in = np.random.uniform(150, 350, n_samples)  # °C
pressure_in = np.random.uniform(50, 300, n_samples)  # bar
permeability = np.random.uniform(0.1, 10, n_samples)  # Darcy
injection_rate = np.random.uniform(10, 500, n_samples)  # kg/s

# Outputs based on synthetic relationships
temperature_out = temperature_in - np.random.uniform(5, 25, n_samples)  # °C
pressure_out = pressure_in - np.random.uniform(1, 10, n_samples)  # bar
energy_extraction_rate = (temperature_out - 100) * injection_rate * permeability * 0.1  # MW

# Economic assumptions
capital_cost = 50000000  # Capital cost in USD
operating_cost_per_year = 2000000  # Operating cost per year in USD
price_per_MW = 1000000  # Price per MW of extracted energy in USD

# Creating a DataFrame
data = pd.DataFrame({
    'Temperature_In': temperature_in,
    'Pressure_In': pressure_in,
    'Permeability': permeability,
    'Injection_Rate': injection_rate,
    'Temperature_Out': temperature_out,
    'Pressure_Out': pressure_out,
    'Energy_Extraction_Rate': energy_extraction_rate
})

# Splitting the dataset
X = data[['Temperature_In', 'Pressure_In', 'Permeability', 'Injection_Rate']]
y = data[['Temperature_Out', 'Pressure_Out', 'Energy_Extraction_Rate']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# PCA for dimensionality reduction
pca = PCA(n_components=3)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Building a Deep Learning model
def build_deep_learning_model():
    model = Sequential()
    model.add(Dense(128, input_dim=X_train_pca.shape[1], activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))  # Output layer (Energy Extraction Rate)
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error', metrics=['mae', 'mse'])
    return model

# Training Deep Learning model
dl_model = build_deep_learning_model()
dl_model.fit(X_train_pca, y_train['Energy_Extraction_Rate'], epochs=200, batch_size=32, validation_split=0.2)

# Predictions with Deep Learning model
y_pred_dl = dl_model.predict(X_test_pca)

# Machine Learning models (XGBoost, LightGBM, Gradient Boosting)
xgb = XGBRegressor(n_estimators=100, random_state=42)
lgbm = lgb.LGBMRegressor(n_estimators=100, random_state=42)
gb = GradientBoostingRegressor(n_estimators=100, random_state=42)

# Fit Machine Learning models
gb.fit(X_train_pca, y_train['Energy_Extraction_Rate'])
xgb.fit(X_train_pca, y_train['Energy_Extraction_Rate'])
lgbm.fit(X_train_pca, y_train['Energy_Extraction_Rate'])

# Predictions for Machine Learning models
y_pred_gb = gb.predict(X_test_pca)
y_pred_xgb = xgb.predict(X_test_pca)
y_pred_lgbm = lgbm.predict(X_test_pca)

# Evaluate performance
mse_dl = mean_squared_error(y_test['Energy_Extraction_Rate'], y_pred_dl)
r2_dl = r2_score(y_test['Energy_Extraction_Rate'], y_pred_dl)

mse_gb = mean_squared_error(y_test['Energy_Extraction_Rate'], y_pred_gb)
r2_gb = r2_score(y_test['Energy_Extraction_Rate'], y_pred_gb)

mse_xgb = mean_squared_error(y_test['Energy_Extraction_Rate'], y_pred_xgb)
r2_xgb = r2_score(y_test['Energy_Extraction_Rate'], y_pred_xgb)

mse_lgbm = mean_squared_error(y_test['Energy_Extraction_Rate'], y_pred_lgbm)
r2_lgbm = r2_score(y_test['Energy_Extraction_Rate'], y_pred_lgbm)

# Calculate ROI and IRR
def calculate_irr_and_roi(capital_cost, operating_cost_per_year, price_per_MW, energy_extraction_rate, years=20):
    # Calculate Revenue
    revenue_per_year = price_per_MW * energy_extraction_rate
    revenue = revenue_per_year * years

    # Calculate Operating Cost
    operating_cost = operating_cost_per_year * years

    # Calculate NPV and ROI
    npv = revenue - (capital_cost + operating_cost)
    roi = npv / capital_cost * 100

    # Approximate IRR using a simplistic approach (Assuming a constant rate of return)
    irr = (revenue / capital_cost) ** (1 / years) - 1
    return npv, roi, irr

# Calculating for the model predictions
npv_dl, roi_dl, irr_dl = calculate_irr_and_roi(capital_cost, operating_cost_per_year, price_per_MW, np.mean(y_pred_dl))
npv_gb, roi_gb, irr_gb = calculate_irr_and_roi(capital_cost, operating_cost_per_year, price_per_MW, np.mean(y_pred_gb))
npv_xgb, roi_xgb, irr_xgb = calculate_irr_and_roi(capital_cost, operating_cost_per_year, price_per_MW, np.mean(y_pred_xgb))
npv_lgbm, roi_lgbm, irr_lgbm = calculate_irr_and_roi(capital_cost, operating_cost_per_year, price_per_MW, np.mean(y_pred_lgbm))

# Print results
print("Deep Learning Model - NPV: ${:,.2f}, ROI: {:.2f}%, IRR: {:.2f}%".format(npv_dl, roi_dl, irr_dl))
print("Gradient Boosting Model - NPV: ${:,.2f}, ROI: {:.2f}%, IRR: {:.2f}%".format(npv_gb, roi_gb, irr_gb))
print("XGBoost Model - NPV: ${:,.2f}, ROI: {:.2f}%, IRR: {:.2f}%".format(npv_xgb, roi_xgb, irr_xgb))
print("LightGBM Model - NPV: ${:,.2f}, ROI: {:.2f}%, IRR: {:.2f}%".format(npv_lgbm, roi_lgbm, irr_lgbm))

# Visualizing results for Model Performance
models = ['Deep Learning', 'Gradient Boosting', 'XGBoost', 'LightGBM']
mse_values = [mse_dl, mse_gb, mse_xgb, mse_lgbm]
r2_values = [r2_dl, r2_gb, r2_xgb, r2_lgbm]

plt.figure(figsize=(12, 6))

# MSE Plot
plt.subplot(1, 2, 1)
plt.bar(models, mse_values, color=['blue', 'green', 'red', 'orange'])
plt.title("MSE for Different Models")
plt.ylabel("Mean Squared Error")

# R² Plot
plt.subplot(1, 2, 2)
plt.bar(models, r2_values, color=['blue', 'green', 'red', 'orange'])
plt.title("R² for Different Models")
plt.ylabel("R² Score")

plt.tight_layout()
plt.show()

# Visualizing Predicted vs Actual Energy Extraction Rate
plt.figure(figsize=(10, 6))
plt.scatter(y_test['Energy_Extraction_Rate'], y_pred_dl, color='blue', label='Deep Learning')
plt.scatter(y_test['Energy_Extraction_Rate'], y_pred_gb, color='green', label='Gradient Boosting')
plt.scatter(y_test['Energy_Extraction_Rate'], y_pred_xgb, color='red', label='XGBoost')
plt.scatter(y_test['Energy_Extraction_Rate'], y_pred_lgbm, color='orange', label='LightGBM')
plt.plot([0, max(y_test['Energy_Extraction_Rate'])], [0, max(y_test['Energy_Extraction_Rate'])], 'k--', label='Perfect Prediction')
plt.xlabel("Actual Energy Extraction Rate (MW)")
plt.ylabel("Predicted Energy Extraction Rate (MW)")
plt.legend()
plt.title("Predicted vs Actual Energy Extraction Rate")
plt.show()

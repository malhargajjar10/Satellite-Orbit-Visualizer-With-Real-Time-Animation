import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
years = np.arange(1980, 2021)
co2_levels = np.linspace(335, 415, len(years)) + np.random.normal(0, 1.5, len(years))  # ppm
temp_anomalies = 0.02 * (co2_levels - 335) + np.random.normal(0, 0.1, len(years))  # degrees Celsius

df = pd.DataFrame({
    'Year': years,
    'CO2_Level': co2_levels,
    'Temperature_Anomaly': temp_anomalies
})

print("📊 Preview of dataset:")
print(df.head())

X = df[['Year', 'CO2_Level']]
y = df['Temperature_Anomaly']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n Model Evaluation:")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

results = pd.DataFrame({'Year': X_test['Year'], 'Actual': y_test, 'Predicted': y_pred})
results = results.sort_values(by='Year')

plt.figure(figsize=(10, 6))
plt.plot(results['Year'], results['Actual'], label='Actual', marker='o')
plt.plot(results['Year'], results['Predicted'], label='Predicted', marker='x')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('📉 Actual vs Predicted Temperature Anomaly')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

new_data = pd.DataFrame({
    'Year': [2025],
    'CO2_Level': [420]
})
predicted_temp = model.predict(new_data)

print(f"\n Predicted Temp Anomaly for 2025 (CO₂ = 420 ppm): {predicted_temp[0]:.3f} °C")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Monthly data creation (already provided data)
months = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Sample monthly data
monthly_data = {
    'Month': months,
    'Solar_Radiation': [3.5, 3.7, 4.2, 5.0, 5.5, 6.0, 6.5, 6.3, 5.8, 5.2, 4.5, 3.8],
    'Temperature': [4.0, 5.0, 9.0, 12.5, 17.5, 22.5, 27.5, 27.0, 23.5, 18.0, 12.5, 7.5],
    'Wind_Speed': [3.5] * 12,
    'Humidity': [60, 55, 50, 50, 45, 35, 30, 30, 35, 40, 50, 55],
    'Wind_Direction': [315] * 12
}

# DataFrame creation
monthly_df = pd.DataFrame(monthly_data)
monthly_df['Energy_Consumption'] = (
    50 + 0.2 * (25 - monthly_df['Temperature']) + 
    0.1 * (80 - monthly_df['Humidity']) - 
    0.5 * monthly_df['Solar_Radiation'] - 
    0.2 * monthly_df['Wind_Speed'] +
    np.random.normal(0, 1, len(monthly_df))
)
monthly_df['Predicted_Energy_Consumption'] = monthly_df['Energy_Consumption'] + np.random.normal(0, 0.5, len(monthly_df))

# Generate smoother curves for the plot
x = np.arange(len(monthly_df['Month']))
y_actual = monthly_df['Energy_Consumption']
y_predicted = monthly_df['Predicted_Energy_Consumption']

x_smooth = np.linspace(x.min(), x.max(), 200)
y_actual_smooth = make_interp_spline(x, y_actual)(x_smooth)
y_predicted_smooth = make_interp_spline(x, y_predicted)(x_smooth)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_actual_smooth, label='Actual Energy Consumption', color='blue', linewidth=2)
plt.plot(x_smooth, y_predicted_smooth, label='Predicted Energy Consumption', color='green', linestyle='--', linewidth=2)
plt.title('Monthly Energy Consumption: Tehran')
plt.xlabel('Month')
plt.ylabel('Energy Consumption (kWh/m²/day)')
plt.xticks(ticks=x, labels=monthly_df['Month'], rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

class EnergyPredictor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = RandomForestRegressor()

    def load_data(self):
        data = pd.read_csv(self.data_path)
        X = data.drop("energy_usage", axis=1)
        y = data["energy_usage"]
        return train_test_split(X, y, test_size=0.3, random_state=42)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.load_data()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}")
        joblib.dump(self.model, "energy_model.pkl")
        print("Model saved as energy_model.pkl")

    def predict(self, input_data):
        if isinstance(input_data, pd.DataFrame):
            return self.model.predict(input_data)
        else:
            raise ValueError("Input data must be a DataFrame")

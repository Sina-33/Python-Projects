from flask import Flask, request, jsonify
import pandas as pd
from models.energy_predictor import EnergyPredictor
from models.energy_allocator import EnergyAllocator

app = Flask(__name__)

predictor = EnergyPredictor("data/energy_usage.csv")
predictor.train_model()

@app.route('/predict_energy', methods=['POST'])
def predict_energy():
    data = request.get_json()
    input_data = pd.DataFrame(data)
    predictions = predictor.predict(input_data)
    return jsonify({"predictions": predictions.tolist()})

@app.route('/optimize_allocation', methods=['POST'])
def optimize_allocation():
    data = request.get_json()
    allocator = EnergyAllocator(data["total_energy"])
    allocation = allocator.optimize_allocation(data["demands"], data["priorities"])
    return jsonify({"allocation": allocation.tolist()})

if __name__ == "__main__":
    app.run(debug=True)

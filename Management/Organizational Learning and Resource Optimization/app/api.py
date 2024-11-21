from flask import Flask, request, jsonify
import pandas as pd
from models.failure_predictor import FailurePredictor
from models.resource_optimizer import ResourceOptimizer

app = Flask(__name__)

failure_predictor = FailurePredictor('data/failed_startups.csv')
failure_predictor.train_model()

@app.route('/predict_failure', methods=['POST'])
def predict_failure():
    data = request.get_json()
    input_data = pd.DataFrame(data)
    predictions = failure_predictor.predict(input_data)
    return jsonify({'predictions': predictions.tolist()})

@app.route('/optimize_resources', methods=['POST'])
def optimize_resources():
    data = request.get_json()
    optimizer = ResourceOptimizer(data['budget'], data['time'], data['people'])
    allocation = optimizer.optimize_allocation(data['priorities'])
    return jsonify({'optimized_allocation': allocation.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

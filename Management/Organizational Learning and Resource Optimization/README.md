# **Organizational Learning and Resource Optimization**

## **Project Overview**
This is a **training project** designed to explore how machine learning and optimization techniques can assist organizations in learning from past failures and optimizing their resource allocations. By combining predictive models, optimization algorithms, and a user-friendly interface, this project aims to demonstrate practical applications of Artificial Intelligence (AI) in organizational decision-making.

The project uses:
- **Machine Learning**: Predict failures of startups based on historical data.
- **Optimization**: Provide recommendations for efficient resource allocation.
- **Web Interface**: A dashboard for visualizing predictions and optimized results.
- **APIs**: RESTful APIs for interacting with predictive and optimization models.

---

## **Key Features**
- **Failure Prediction**:
  - A machine learning model built using Random Forest Classifier predicts the probability of startup failures based on input features.
  - Fine-tuned to process tabular data such as financial indicators, team size, or market conditions.

- **Resource Optimization**:
  - A linear programming-based model recommends optimal allocation of resources (e.g., budget, time, and workforce).
  - Takes into account user-defined priorities for different resource types.

- **Interactive Dashboard**:
  - An easy-to-use web interface built with Flask and styled with CSS for enhanced user experience.
  - Features forms for submitting input data and sections for viewing predictions and optimization results.

- **RESTful APIs**:
  - `/predict_failure`: Accepts JSON input and returns failure predictions.
  - `/optimize_resources`: Accepts JSON input for resource constraints and returns optimized allocations.

---

## **Project Structure**
```
📁 organizational-learning
   ├── data/
   │   ├── failed_startups.csv       # Historical data for training the failure prediction model
   ├── models/
   │   ├── failure_predictor.py      # Failure prediction model (Random Forest)
   │   ├── resource_optimizer.py     # Resource optimization model (Linear Programming)
   ├── app/
   │   ├── api.py                    # Flask API exposing models
   │   ├── static/
   │   │   └── style.css             # CSS for dashboard styling
   │   ├── templates/
   │   │   └── dashboard.html        # HTML for the interactive dashboard
   ├── requirements.txt              # List of required Python libraries
   └── README.md                     # Project documentation
```

---

## **How to Set Up and Run**

### **1. Prerequisites**
Ensure the following are installed:
- **Python 3.8+**
- **Pip** (Python package manager)

### **2. Install Dependencies**
Navigate to the project directory and install required libraries:
```bash
pip install -r requirements.txt
```

### **3. Train the Models**
(Optional) If you wish to retrain the failure prediction model:
```bash
python -m models.failure_predictor
```

### **4. Run the Application**
Start the Flask server to host the API and dashboard:
```bash
python app/api.py
```

### **5. Access the Dashboard**
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

### **6. API Endpoints**
- **Failure Prediction**: Send a POST request to `/predict_failure` with JSON data containing feature values.
- **Resource Optimization**: Send a POST request to `/optimize_resources` with JSON data containing constraints and priorities.

---

## **Example Usage**

### **Failure Prediction**
**Input:**
```json
[
    {"feature1": 5, "feature2": 10},
    {"feature1": 3, "feature2": 7}
]
```

**Response:**
```json
{
    "predictions": [1, 0]
}
```

---

### **Resource Optimization**
**Input:**
```json
{
    "budget": 100,
    "time": 50,
    "people": 10,
    "priorities": [0.8, 0.6, 0.7]
}
```

**Response:**
```json
{
    "optimized_allocation": [30, 40, 20]
}
```

---

## **Project Objectives**
This project is primarily designed as a **learning tool** for:
1. Practicing **machine learning workflows** using real-world-like data.
2. Exploring **optimization techniques** such as linear programming.
3. Building **end-to-end applications** that integrate APIs, machine learning, and frontend design.
4. Developing **RESTful APIs** for easy interaction with predictive and optimization models.

---

## **Technologies Used**
- **Python**: Core programming language for models and API.
- **Flask**: For serving the API and web dashboard.
- **Scikit-learn**: For training and evaluating machine learning models.
- **SciPy**: For implementing linear programming in the optimization model.
- **HTML/CSS**: For designing and styling the web dashboard.

---

## **Future Enhancements**
- **Enhanced Data Visualization**:
  - Use libraries like Plotly or D3.js for dynamic charts and graphs.
- **Advanced Machine Learning Models**:
  - Incorporate deep learning models for more complex predictions.
- **Support for Additional Data Types**:
  - Include text data (e.g., customer feedback) for richer feature engineering.
- **Real-time Processing**:
  - Implement WebSocket-based real-time interactions for instant feedback.

---

## **Contact**
For questions or feedback:
- **Email**: [sina.engr@gmail.com](mailto:sina.engr@gmail.com)
- **GitHub**: [Sina-33](https://github.com/Sina-33)

--- 

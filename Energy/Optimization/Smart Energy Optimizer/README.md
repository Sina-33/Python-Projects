# **Smart Energy Optimizer**

## **Overview**
The **Smart Energy Optimizer** is an experimental project aimed at exploring the integration of machine learning and optimization techniques to enhance energy management. The project predicts energy consumption and optimizes resource allocation based on user-defined constraints and priorities. Designed as a training exercise, this project demonstrates practical applications of Artificial Intelligence (AI) in the field of energy management.

---

## **Key Features**
1. **Energy Consumption Prediction**:
   - Leverages a machine learning model (Random Forest) to forecast energy usage based on historical data.
   - Considers factors such as time of day, temperature, and more.

2. **Energy Allocation Optimization**:
   - Uses linear programming to allocate energy efficiently across different sectors or regions.
   - Prioritizes resources based on user-defined weights, such as cost, environmental impact, or energy source.

3. **RESTful APIs**:
   - **`/predict_energy`**: Accepts JSON data and predicts energy consumption for specified scenarios.
   - **`/optimize_allocation`**: Takes user constraints and priorities to recommend an optimal energy distribution strategy.

4. **Interactive Dashboard**:
   - A user-friendly web interface for visualizing predictions and optimization results.
   - Features input forms for submitting data and dynamic sections for displaying results.

---

## **Project Structure**
```
📁 smart-energy-optimizer
   ├── data/
   │   ├── energy_usage.csv          # Historical energy consumption data
   ├── models/
   │   ├── energy_predictor.py       # Energy consumption prediction model
   │   ├── energy_allocator.py       # Energy allocation optimization model
   ├── app/
   │   ├── api.py                    # Flask API for models
   │   ├── static/
   │   │   └── style.css             # CSS for dashboard styling
   │   ├── templates/
   │   │   └── dashboard.html        # Interactive dashboard HTML
   ├── requirements.txt              # Python dependencies
   └── README.md                     # Project documentation
```

---

## **Setup and Installation**

### **1. Prerequisites**
- Python 3.8+
- Pip (Python package manager)

### **2. Install Dependencies**
Run the following command to install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **3. Start the Application**
To launch the Flask API and dashboard, run:
```bash
python app/api.py
```

### **4. Access the Dashboard**
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## **Usage**

### **1. Energy Consumption Prediction**
#### API Endpoint: `/predict_energy`
Send a POST request with JSON data containing feature values such as temperature and time of day.

**Sample Input**:
```json
[
    {"temperature": 22, "time_of_day": 10},
    {"temperature": 24, "time_of_day": 15}
]
```

**Sample Response**:
```json
{
    "predictions": [280, 350]
}
```

---

### **2. Energy Allocation Optimization**
#### API Endpoint: `/optimize_allocation`
Send a POST request with total available energy, sector demands, and priority weights.

**Sample Input**:
```json
{
    "total_energy": 1000,
    "demands": [300, 400, 500],
    "priorities": [0.8, 0.7, 0.6]
}
```

**Sample Response**:
```json
{
    "allocation": [333.33, 333.33, 333.33]
}
```

---

### **3. Interactive Dashboard**
The dashboard provides:
- **Energy Prediction**: Input historical data to predict future energy consumption.
- **Optimization Results**: Visualize the allocation of energy resources based on priorities.

---

## **Technologies Used**
- **Python**: Core programming language.
- **Flask**: API and dashboard backend.
- **Scikit-learn**: Machine learning library for energy prediction.
- **SciPy**: For linear programming in optimization.
- **HTML/CSS**: Dashboard design and styling.

---

## **Project Objectives**
This project is a **training and experimental initiative** aimed at:
1. Understanding machine learning workflows in energy prediction.
2. Exploring linear programming for resource optimization.
3. Demonstrating the integration of AI and optimization with web-based user interfaces.

---

## **Limitations**
- **Experimental Data**: The project uses synthetic or limited data; accuracy may vary with real-world datasets.
- **Scalability**: The current implementation is designed for educational purposes and may require additional optimizations for large-scale use.

---

## **Future Enhancements**
1. **Incorporate IoT Data**:
   - Collect real-time energy data from smart meters and other devices.
2. **Integrate Renewable Energy**:
   - Add support for renewable energy sources (e.g., solar, wind).
3. **Enhanced Visualizations**:
   - Use libraries like Plotly for interactive charts and graphs.
4. **Advanced Machine Learning**:
   - Implement deep learning models like LSTMs for time-series energy prediction.

---

## **Contact**
For questions or feedback:
- **Email**: [sina.engr@gmail.com](mailto:sina.engr@gmail.com)
- **GitHub**: [Sina-33](https://github.com/Sina-33)

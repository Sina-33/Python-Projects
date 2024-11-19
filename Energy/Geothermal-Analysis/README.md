### Geothermal Energy Extraction Prediction and Economic Analysis

#### Overview
This project focuses on analyzing geothermal energy extraction systems. The main objective is to predict the energy extraction rate and conduct an economic analysis of these systems using advanced machine learning models and evaluating financial indicators such as **NPV** (Net Present Value), **ROI** (Return on Investment), and **IRR** (Internal Rate of Return).

#### Input and Output Variables
- **Inputs**:
  - **Temperature_In**: The input temperature of water or steam entering the system, based on the geothermal source temperature.
  - **Pressure_In**: The pressure entering the system, which has a significant impact on extraction efficiency.
  - **Permeability**: The permeability of underground rocks, indicating the ability of fluids to pass through them.
  - **Injection_Rate**: The rate at which fluid is injected into the system.

- **Outputs**:
  - **Temperature_Out**: The temperature of the fluid leaving the system.
  - **Pressure_Out**: The pressure of the fluid leaving the system.
  - **Energy_Extraction_Rate**: The amount of energy extracted from the geothermal system, measured in megawatts (MW).

#### Prediction Models
For predicting energy extraction rates, four advanced machine learning models were employed: **Deep Learning**, **Gradient Boosting**, **XGBoost**, and **LightGBM**.

1. **Deep Learning**:
   - A neural network with multiple layers that automatically extracts features from input data and predicts the energy extraction rate. These networks are especially suitable for nonlinear and complex data.

2. **Gradient Boosting**:
   - A model based on the iterative construction of decision trees that are sequentially boosted to improve performance. It is particularly useful for handling noisy and complex data.

3. **XGBoost**:
   - An improved version of **Gradient Boosting**, incorporating techniques like pruning and regularization for enhanced model performance and better prediction accuracy.

4. **LightGBM**:
   - A decision tree-based algorithm that uses techniques to accelerate learning, making it highly suitable for large datasets.

#### Economic Analysis
In addition to predicting energy extraction rates, the project also conducts an economic analysis of geothermal systems. The three key financial indicators calculated are:

1. **NPV (Net Present Value)**:
   - Represents the current value of a project, accounting for future revenues and current costs. A positive NPV indicates profitability.
   - NPV Formula:
     \[
     NPV = \sum \frac{R_t}{(1 + r)^t} - C_0
     \]
     Where:
     - \( R_t \) is the revenue at time \( t \),
     - \( r \) is the discount rate,
     - \( C_0 \) is the initial investment cost.

2. **ROI (Return on Investment)**:
   - Indicates the percentage return on investment and profitability of the project. The ROI formula is:
     \[
     ROI = \frac{NPV}{C_0} \times 100
     \]
     Where \( C_0 \) is the initial project cost.

3. **IRR (Internal Rate of Return)**:
   - The rate of return that makes the NPV of the project zero. This value is typically computed using numerical methods like the **Newton-Raphson method**.

#### Model Evaluation
To evaluate the prediction performance, two key metrics were used:

- **MSE (Mean Squared Error)**:
  - Indicates the average squared differences between the predicted and actual values. A lower value means better model performance.

- **R² (R-squared)**:
  - Measures the correlation between the predicted and actual data. An R² value close to 1 indicates a strong match between the model and real data.

#### Results Analysis
The prediction and evaluation results of the models for energy extraction rates were examined. For each model, the **MSE** and **R²** values were calculated to determine which model provided the most accurate predictions. Additionally, the **NPV**, **ROI**, and **IRR** values were computed for economic assessment, helping inform investment decisions for geothermal projects.

#### Results Visualization
Various charts were generated to display the results:
- **MSE Chart**: To show the model accuracies.
- **R² Chart**: To evaluate how well the models fit the actual data.
- **Predicted vs Actual Chart**: To compare model predictions against real data.

#### Conclusion
This project provides a comprehensive analysis of geothermal energy extraction systems, combining energy extraction predictions with detailed economic evaluations. By utilizing advanced machine learning models and economic analysis tools, better decisions can be made for investments in geothermal energy projects. This project can serve as a useful tool for optimizing and analyzing geothermal energy extraction systems in the energy industry.

### Code Structure
- **Library Imports**: Standard libraries for data processing, predictions, and machine learning models.
- **Data Simulation**: Synthetic data for inputs and outputs were generated.
- **Model Training**: Machine learning and deep learning models were trained for prediction.
- **Economic Analysis**: Calculated financial metrics such as **NPV**, **ROI**, and **IRR**.
- **Model Evaluation**: MSE and R² metrics were used to evaluate model performance.
- **Results Visualization**: Plots were generated to display model performance and economic analysis results.

# **Investor Behavior Prediction**

## **Project Overview**
This project is a **training exercise** to explore the application of Natural Language Processing (NLP) and Machine Learning in analyzing financial news and predicting investor behavior. It uses **BERT** for sentiment analysis, integrates with **NewsAPI** for real-time news fetching, and employs a RESTful API built with Flask for live predictions.

---

## **Key Features**
- **Fine-tuned BERT Model:** Utilizes a pre-trained BERT model for sentiment analysis, fine-tuned on financial news headlines.
- **Real-Time News Fetching:** Retrieves up-to-date news articles using NewsAPI.
- **Flask API Integration:** Provides RESTful API endpoints for live predictions.
- **Scalable Design:** Modular architecture for easy extension and integration.
- **Multi-Category Sentiment Prediction:** Supports classification into "Positive" or "Negative" sentiment categories.

---

## **Project Structure**
```
📁 investor-behavior
   ├── app.py               # Flask API for predictions
   ├── bert_model.py        # Fine-tuned BERT model for sentiment classification
   ├── fetch_news.py        # Script for fetching real-time news using NewsAPI
   ├── train_model.py       # Script to train and fine-tune BERT model
   ├── requirements.txt     # List of dependencies
   └── README.md            # Project description
```

---

## **How to Set Up and Run**

### **1. Prerequisites**
Ensure you have Python 3.9+ installed on your system.

### **2. Install Dependencies**
Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```

### **3. Train the Model (Optional)**
You can train or fine-tune the BERT model using the provided `train_model.py` script:
```bash
python train_model.py
```

### **4. Run the Flask API**
Start the Flask server to serve the predictions:
```bash
python app.py
```

### **5. Test the API**
Use a tool like Postman or your browser to make a GET request to the following endpoint:
```
http://127.0.0.1:5000/predict?query=stock market
```

#### Example Response:
```json
[
    {
        "news": "Stock prices rise due to strong earnings reports.",
        "prediction": "Positive"
    },
    {
        "news": "Market uncertainty increases amid inflation fears.",
        "prediction": "Negative"
    }
]
```

---

## **Dependencies**
- **Python 3.9+**
- **Transformers**: NLP library for working with BERT and other Transformer models.
- **PyTorch**: For running and fine-tuning the BERT model.
- **Flask**: To build a RESTful API for predictions.
- **Scikit-learn**: For evaluation and auxiliary tasks.
- **Pandas**: For data manipulation.
- **Requests**: For fetching real-time news data from APIs.

Install all dependencies using the `requirements.txt` file.

---

## **How It Works**
1. **Fetch News:** The `fetch_news.py` script connects to the **NewsAPI** and retrieves headlines based on a query (e.g., "stock market").
2. **Process with BERT:** The headlines are tokenized and passed through a fine-tuned BERT model, which classifies each headline as either "Positive" or "Negative."
3. **API Response:** The Flask API returns the predictions in JSON format for easy integration into other systems.

---

## **Future Improvements**
- **Dashboard Integration:** Create an interactive dashboard for visualizing predictions and sentiment trends.
- **Support for Multi-Class Sentiment:** Extend the model to classify more granular sentiments like "Neutral" or "Highly Positive."
- **Real-Time Predictions:** Implement WebSocket or other real-time communication protocols.
- **Larger Dataset:** Fine-tune the model further using a larger and more diverse financial dataset.

---

## **Contributing**
This is a training project. Contributions are welcome for further improvement and exploration.

---

## **Contact**
For questions or feedback, feel free to reach out:
- **Email:** [sina.engr@gmail.com](mailto:sina.engr@gmail.com)
- **GitHub:** [Sina-33](https://github.com/Sina-33)

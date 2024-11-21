from flask import Flask, request, jsonify
from fetch_news import fetch_news
from bert_model import predict_news

app = Flask(__name__)

# API Key for NewsAPI
NEWS_API_KEY = "your_api_key_here"

@app.route('/predict', methods=['GET'])
def predict():
    query = request.args.get('query', 'stock market')
    try:
        news_titles = fetch_news(NEWS_API_KEY, query, page_size=5)
        predictions = predict_news(news_titles)
        response = [{"news": title, "prediction": "Positive" if pred == 1 else "Negative"} for title, pred in zip(news_titles, predictions)]
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


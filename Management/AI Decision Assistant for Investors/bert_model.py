from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load Fine-Tuned Model
tokenizer = BertTokenizer.from_pretrained("./fine_tuned_bert")
model = BertForSequenceClassification.from_pretrained("./fine_tuned_bert")

def predict_news(news_list):
    inputs = tokenizer(news_list, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, axis=-1)
    return predictions.numpy().tolist()


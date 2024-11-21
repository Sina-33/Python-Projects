from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
import torch
import pandas as pd

# Load Data (Replace this with real data)
data = {
    "news": [
        "Stock prices are expected to rise due to strong earnings reports.",
        "Market uncertainty increases as inflation fears grow.",
        "Tech companies see major sell-off after poor quarterly results.",
        "Investors optimistic about the recovery of the travel industry."
    ],
    "label": [1, 0, 0, 1]  # 1: Positive, 0: Negative
}
df = pd.DataFrame(data)

# Tokenizer and Model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Tokenize Data
def tokenize_data(news):
    return tokenizer(news, padding=True, truncation=True, max_length=512, return_tensors="pt")

tokens = df['news'].apply(lambda x: tokenize_data(x))
labels = torch.tensor(df['label'].values)

# Train-Test Split
train_texts, test_texts, train_labels, test_labels = train_test_split(tokens, labels, test_size=0.25, random_state=42)

# Training Arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir='./logs',
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset={'input_ids': train_texts, 'labels': train_labels},
    eval_dataset={'input_ids': test_texts, 'labels': test_labels},
)

# Train the Model
trainer.train()

# Save the Fine-Tuned Model
model.save_pretrained("./fine_tuned_bert")
tokenizer.save_pretrained("./fine_tuned_bert")


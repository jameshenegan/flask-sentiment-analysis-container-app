from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment-analysis model during app startup
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['text_input']

    # Perform sentiment analysis on the user input
    result = sentiment_pipeline(user_input)
    sentiment = result[0]['label']
    confidence = result[0]['score']

    # Display the result with sentiment and confidence score
    return f"Sentiment: {sentiment}<br>Confidence: {confidence}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

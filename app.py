from flask import Flask, render_template, request
from transformers import pipeline
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load the sentiment-analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def parse_conversation(text):
    # Split the input text into lines and parse each line
    lines = text.strip().split('\n')
    conversation = []
    position = 1
    
    for line in lines:
        # Parse each line for "Author: Message"
        if ':' in line:
            author, message = line.split(':', 1)
            author = author.strip()
            message = message.strip()
            sentiment_result = sentiment_pipeline(message)[0]
            sentiment_score = sentiment_result['score'] if sentiment_result['label'] == 'POSITIVE' else -sentiment_result['score']
            
            # Append the parsed data as a dictionary to the conversation list
            conversation.append({
                "position": position,
                "author": author,
                "text": message,
                "sentiment_score": sentiment_score
            })
            position += 1

    return conversation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    text = request.form['single_text']
    result = sentiment_pipeline(text)[0]
    sentiment = result['label']
    confidence = result['score']
    return render_template('results_single.html', sentiment=sentiment, confidence=confidence)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Get the input text from the form
    text = request.form['conversation_text']
    conversation = parse_conversation(text)
    
    # Separate the data for plotting
    customer_positions = [entry["position"] for entry in conversation if entry["author"] == "Customer"]
    customer_sentiments = [entry["sentiment_score"] for entry in conversation if entry["author"] == "Customer"]
    agent_positions = [entry["position"] for entry in conversation if entry["author"] == "Agent"]
    agent_sentiments = [entry["sentiment_score"] for entry in conversation if entry["author"] == "Agent"]

    # Plot the sentiment progression over the conversation
    plt.figure(figsize=(10, 5))
    plt.plot(customer_positions, customer_sentiments, label="Customer Sentiment", marker='o')
    plt.plot(agent_positions, agent_sentiments, label="Agent Sentiment", marker='o')
    plt.xlabel('Position in Conversation')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Progression of Customer and Agent')
    plt.legend()
    plt.grid(True)
    
    # Save plot to static directory
    plt.savefig('static/sentiment_plot.png')
    plt.close()

    return render_template('results_conversation.html', conversation=conversation, image_path='static/sentiment_plot.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

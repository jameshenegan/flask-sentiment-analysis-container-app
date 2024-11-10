# Flask Sentiment Analysis Container App

This project is a Flask-based web application that performs sentiment analysis on user-submitted text using a pre-trained **DistilBERT** model from the **Transformers** library. The application is containerized using Docker, making it easy to deploy and run on any platform with Docker support.

## Features

- **Sentiment Analysis**: Leverages a pre-trained model (`distilbert-base-uncased-finetuned-sst-2-english`) to analyze the sentiment of text input.
- **Flask Web Interface**: Provides a simple web interface for text input and displays the sentiment and confidence score.
- **Dockerized**: The application is containerized for easy deployment and isolation of dependencies.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- Optional: Familiarity with Python, Flask, and basic Docker commands.

## Project Structure

```plaintext
.
├── Dockerfile           # Docker setup file to build the application image
├── requirements.txt     # List of Python dependencies
├── app.py               # Flask application code
├── templates/
│   └── index.html       # HTML template for the web interface
└── README.md            # Documentation
```

## Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine.

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Build the Docker Image

Build the Docker image from the `Dockerfile`. This image includes all dependencies and downloads the sentiment analysis model during the build process.

```bash
docker build -t flask-sentiment-app .
```

### 3. Run the Docker Container

Run the container, exposing the app on port 5050. The `-p 5050:5050` flag maps the container’s port 5050 to your machine’s port 5050.

```bash
docker run -p 5050:5050 flask-sentiment-app
```

The app will be accessible at `http://localhost:5050`.

### 4. Access the Web Application

Navigate to `http://localhost:5050` in your web browser. You should see a simple form where you can input text for sentiment analysis.

## Application Usage

1. **Enter Text**: Input the text you want to analyze in the provided text area.
2. **Submit**: Click the "Submit" button.
3. **View Results**: The app will display the sentiment (e.g., positive, negative) along with the confidence score for the prediction.

## Example

To test the sentiment analysis, try entering a sentence such as:

> "I love using this app for sentiment analysis!"

The app should return a sentiment label (e.g., "POSITIVE") and a confidence score.

## Files

- **app.py**: Main Flask application code. It initializes the sentiment analysis model and handles HTTP routes.
- **Dockerfile**: Defines the Docker image, including installing dependencies and downloading the model.
- **requirements.txt**: Lists the Python libraries required by the app.
- **templates/index.html**: HTML template for the user interface.

## Troubleshooting

- **Error: Model not found**: If the container fails due to model loading issues, make sure your `requirements.txt` includes the correct versions of `transformers` and `torch`.
- **Docker Build Fails**: Ensure Docker is running and you have a stable internet connection, as the model download happens during the build process.
- **Flask Debug Mode**: By default, Flask is set to debug mode. For production environments, set `debug=False` in `app.py`.

## Additional Resources

- [Transformers Documentation](https://huggingface.co/transformers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)

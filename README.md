# Flask Sentiment Analysis Conversation App

This project is a Flask-based web application for analyzing the sentiment of a conversation between a customer and an agent. Using a pre-trained **DistilBERT** model from the **Transformers** library, the app performs sentiment analysis on each message and visualizes the sentiment progression over the conversation.

## Features

- **Sentiment Analysis**: Analyzes sentiment on each message in a customer-agent conversation, showing positive or negative sentiment.
- **Visualization**: Generates a plot of sentiment progression throughout the conversation.
- **Flask Web Interface**: Provides a user-friendly interface to input conversation data and view analysis results.
- **Dockerized**: The application is containerized with Docker for easy deployment.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed.
- Familiarity with Docker commands and Python (optional but helpful).

## Project Structure

```plaintext
.
├── Dockerfile           # Docker setup for building the application image
├── requirements.txt     # List of Python dependencies
├── app.py               # Flask application code
├── templates/
│   ├── index.html       # HTML template for the input page
│   └── results.html     # HTML template for displaying results
└── README.md            # Documentation
```

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Build the Docker Image

Build the Docker image, which installs all dependencies and downloads the sentiment analysis model:

```bash
docker build -t flask-sentiment-app .
```

### 3. Run the Docker Container

Run the container and map port 5050 from the container to your local machine:

```bash
docker run -p 5050:5050 flask-sentiment-app
```

The application will be available at `http://localhost:5050`.

### 4. Access the Web Application

Go to `http://localhost:5050` in your browser. Enter a conversation where each line follows the format `"Author: Message"`, then click "Submit" to analyze the conversation.

## Application Usage

1. **Enter Conversation**: Input text where each line follows the format `Author: Message`. For example:

   ```
   Customer: Hi, I need help with my account.
   Agent: Sure, I'd be happy to assist you.
   Customer: Thanks, I'm feeling frustrated because I can't log in.
   Agent: I understand, let's get that sorted out for you.
   ```

2. **Analyze**: Click "Submit" to process the conversation.

3. **View Results**: The application will display:
   - A plot showing sentiment progression for both the customer and agent over the conversation.
   - A detailed list of each message with its sentiment score.

## Example

For a conversation such as:

```
Customer: This is the best service!
Agent: Thank you for the feedback!
Customer: But I had an issue with my last order.
Agent: I'm here to help resolve that.
```

The app will show a plot where each message is labeled with its sentiment score. Positive messages have positive scores, while negative messages have negative scores.

## Files

- **app.py**: Main Flask application. Initializes the sentiment analysis model, parses conversation data, and generates sentiment visualizations.
- **Dockerfile**: Configures the Docker environment, installs dependencies, and downloads the model.
- **requirements.txt**: Lists required Python packages.
- **templates/index.html**: HTML form for entering conversation data.
- **templates/results.html**: Displays sentiment analysis results and plot.

## Troubleshooting

- **Plot Not Displaying**: Ensure the `matplotlib` library is correctly installed and that the static directory is accessible.
- **Model Loading Errors**: Verify internet connectivity, as the model downloads during Docker build.
- **Docker Build Fails**: Ensure Docker is installed and running, and check for network issues.

## Additional Resources

- [Transformers Documentation](https://huggingface.co/transformers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Docker Documentation](https://docs.docker.com/)

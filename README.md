# Flask Sentiment Analysis App

This project is a Flask-based web application that performs sentiment analysis. It offers two modes of analysis:

1. **Single Block of Text Classification**: Classifies the sentiment of a single text block.
2. **Conversation Analysis and Visualization**: Analyzes the sentiment progression of a conversation between a customer and an agent, displaying a visualization of sentiment changes over time.

The app uses a pre-trained **DistilBERT** model from the **Transformers** library for sentiment analysis and **Matplotlib** for visualization. The application is containerized with Docker for easy deployment.

## Features

- **Sentiment Analysis**:
  - **Single Text Classification**: Analyzes the sentiment of a single paragraph or sentence.
  - **Conversation Analysis**: Tracks and visualizes sentiment progression in a conversation, displaying results in a line chart.
- **Flask Web Interface**: A user-friendly web page with two separate input options to choose between text classification and conversation analysis.
- **Dockerized**: The application is containerized, making deployment easy and reliable.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.

## Project Structure

```plaintext
.
├── Dockerfile           # Docker setup for building the application image
├── requirements.txt     # List of Python dependencies
├── app.py               # Flask application code
├── templates/
│   ├── index.html       # HTML template for the main input page
│   ├── results_single.html  # HTML template for displaying single text classification results
│   └── results_conversation.html # HTML template for displaying conversation analysis results
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

Build the Docker image using the `Dockerfile`. This process installs all dependencies and downloads the sentiment analysis model.

```bash
docker build -t flask-sentiment-app .
```

### 3. Run the Docker Container

Run the container and map port 5050 to make the app accessible at `http://localhost:5050`.

```bash
docker run -p 5050:5050 flask-sentiment-app
```

### 4. Access the Web Application

Navigate to `http://localhost:5050` in your web browser to access the app.

## Application Usage

1. **Classify a Block of Text**:

   - Enter a paragraph or sentence in the **"Classify a Block of Text"** text box.
   - Click **"Classify Text"** to analyze the sentiment.
   - The result will display the sentiment label (e.g., POSITIVE or NEGATIVE) and the confidence score.

2. **Analyze a Conversation**:
   - Enter a conversation in the format `"Author: Message"` in the **"Analyze a Conversation"** text box.
   - Each line should represent one message in the conversation, with the format `"Customer: message"` or `"Agent: message"`.
   - Click **"Analyze Conversation"** to analyze the conversation.
   - The result page displays:
     - A line chart showing the sentiment progression for each author.
     - A breakdown of each message with its sentiment score.

### Example Inputs

#### **Single Block of Text**:

##### Example 1

```
The weather is nice today.
```

##### Example 2

```
I am not feeling well.
```

##### Example 3

```
I sent you a message on Teams.
```

#### **Conversation**:

#### Example 1

```
Customer: I've been having trouble with my account for a few days now.
Agent: I’m here to help. Could you tell me a bit more about the issue?
Customer: Well, I keep getting locked out every time I try to log in.
Agent: I understand how frustrating that can be. Let's see what we can do.
Customer: I hope you can fix it soon. This has been really annoying.
Agent: I’ll do my best. Have you tried resetting your password?
Customer: Yes, but it still doesn’t let me in even after I reset it.
Agent: I see. I’ll check to see if there’s any lock on your account.
Customer: Okay, please. I need to access my account urgently.
Agent: I’ve checked, and it looks like there’s a security flag on your account. I’ll remove it now.
Customer: Thank you, that would be great.
Agent: I’ve removed the flag. Could you try logging in again?
Customer: Sure, I’ll give it a try now.
Agent: Let me know if it works.
Customer: It worked! Thank you so much for your help.
Agent: I’m happy to hear that! Is there anything else I can assist you with?
Customer: No, that was my main issue. I’m really glad it’s resolved.
Agent: Great to know. If you ever need help again, don’t hesitate to reach out.
Customer: Thank you, I appreciate that.
Agent: You’re very welcome. Have a great day!
```

#### Example 2

```
Customer: My internet has been cutting out a lot lately.
Agent: I’m sorry to hear that. How long has this been happening?
Customer: About a week now, and it’s really affecting my work.
Agent: I understand. Let’s look into it right away.
Customer: I hope we can fix it quickly. I’ve already tried restarting the router.
Agent: Good call. I’ll run some diagnostics on our end.
Customer: Thanks, I really need a stable connection.
Agent: It looks like there might be an issue with the signal strength. I’ll adjust some settings.
Customer: I’d appreciate that. It’s been so frustrating.
Agent: I can imagine. Let me make a few adjustments.
Customer: Alright, please do.
Agent: I’ve adjusted the settings. Can you try browsing a few sites to see if it’s working better?
Customer: Sure, let me try. Hold on a second.
Agent: Take your time. I’ll be here.
Customer: It still doesn't work.  I'm so angry right now.
Agent: I am sorry to hear that.
Customer: I plan on discontinuing my service.  Thanks for nothing.
```

## Files

- **app.py**: Main Flask application code. It initializes the sentiment analysis model, provides routes for each type of analysis, and generates sentiment visualizations for conversations.
- **Dockerfile**: Configures the Docker environment, installs dependencies, and downloads the model.
- **requirements.txt**: Lists required Python packages.
- **templates/index.html**: Main input page where users can select their analysis type.
- **templates/results_single.html**: Displays the result for single text classification.
- **templates/results_conversation.html**: Displays the sentiment progression plot and detailed analysis for conversations.

## Troubleshooting

- **Plot Not Displaying**: Ensure `matplotlib` is correctly installed and that the `static` directory is accessible.
- **Model Loading Errors**: Verify internet connectivity during Docker build as the model downloads at this stage.
- **Docker Build Fails**: Ensure Docker is installed, running, and check network connectivity.

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Docker Documentation](https://docs.docker.com/)
- [Transformers Documentation](https://github.com/huggingface/transformers)

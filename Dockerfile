# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements and application files into the container
COPY requirements.txt requirements.txt
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download the model during build time
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

# Expose port 5050 for Flask
EXPOSE 5050

# Set the entry point to run the app
CMD ["python", "app.py"]


# Sentiment Analysis Web Application

This is a simple Flask web application that uses a sentiment analysis API to analyze the sentiment of a given text.

## How it works

The application has two main routes:

1. `/` (GET): This route renders an HTML form where users can input text to be analyzed.

2. `/analyze` (POST): This route receives the text from the form, sends it to a sentiment analysis API, and returns the analysis result.

The sentiment analysis API endpoint and key are fetched from environment variables `CONTAINER_API_URL` and `API_KEY` respectively.

## Setup

To run this application, you need to have Python and Flask installed. You also need to set the environment variables `CONTAINER_API_URL` and `API_KEY` with your sentiment analysis API endpoint and key.

## Running the application

You can run the application using the following command:

```bash
python app.py
```

This will start a web server on your local machine. You can access the application by navigating to `http://localhost:5000` in your web browser.

## Error handling

The application has basic error handling:

- If no text is provided for analysis, it returns a 400 error with the message "No text provided".
- If the API configuration is not set, it returns a 500 error with the message "API configuration not set".
- If the sentiment analysis API request fails, it returns the HTTP status code from the API with the message "Failed to analyze sentiment".

## Docker Deployment

This application can also be run in a Docker container. The provided Dockerfile sets up a Python environment, installs the necessary dependencies, and starts the application.

### Dockerfile Details

- The Dockerfile uses the official Python 3.11 Alpine image as a base.
- The working directory in the container is set to `/app`.
- The application's files are copied into the container at `/app`.
- The necessary Python packages are installed using the `requirements.txt` file.
- Port 5001 is exposed for the application.
- Two environment variables, `CONTAINER_API_URL` and `API_KEY`, are set for the sentiment analysis API endpoint and key.
- When the container is launched, `app.py` is run to start the application.

### Building the Docker Image

You can build the Docker image using the following command:

```bash
docker build -t sentiment-analysis-app .
```

### Running the Docker Container

You can run the Docker container using the following command:

```bash
docker run -p 5001:5001 sentiment-analysis-app
```

This will start the application and make it accessible at `http://localhost:5001` in your web browser.

## Hosting

The web application is hosted on Azure and can be accessed at the following URL:

[ai-py-demox.azurewebsites.net](http://ai-py-demox.azurewebsites.net)

Please note that the hosted version of the application uses the same sentiment analysis API as the local version, so the API configuration must be set correctly for the hosted version to work.
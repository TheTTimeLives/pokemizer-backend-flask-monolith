# Use the Python 3.8 base image
FROM python:3.8

# Set the working directory in the Docker image
WORKDIR /app

# Copy the requirements.txt file to the Docker image
COPY requirements.txt .

# Install the Python dependencies using pip
RUN pip install -r requirements.txt

# Copy the Flask app code to the Docker image
COPY app.py .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]

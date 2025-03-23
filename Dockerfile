# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary ports
EXPOSE 8080 8501

# Start Flask API and Streamlit UI
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8080 server:app & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]

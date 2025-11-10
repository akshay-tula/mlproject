# Use a Python 3.9 image optimized for size
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list and install them first (Docker caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
# This includes src/, templates/, app.py, and artifact/
COPY . .

# --- START FIX: Update Flask App name ---
# Set the environment variable for Flask to point to the new file name
ENV FLASK_APP=application.py

# Start the application using Gunicorn (a robust production server)
# 'application:application' points to the 'application' object inside application.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "application:application"]
# --- END FIX ---

EXPOSE 5000
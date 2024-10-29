FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Flask directly
RUN pip install --no-cache-dir Flask

# Copy the application code
COPY ./templates ./templates
COPY app.py ./

# Expose the Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and folders
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Expose port and run
EXPOSE 5000
CMD ["python", "app.py"]

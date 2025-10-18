FROM python:3.10-slim

# Set working directory
WORKDIR /workspace

# Copy requirements first for caching
COPY ./app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder
COPY ./app/ .

# Expose Streamlit default port
EXPOSE 8501

# Default command for container
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

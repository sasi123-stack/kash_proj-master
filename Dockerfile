FROM python:3.9-slim

# Set up environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=7860 \
    APP_HOME=/app

WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn uvicorn

# Copy the rest of the application
COPY . .

# Hugging Face Spaces expects a user with ID 1000
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Create model cache directory with correct permissions
RUN mkdir -p $HOME/app/models && chmod 777 $HOME/app/models
ENV MODEL_CACHE_DIR=$HOME/app/models

# Expose the default Hugging Face port
EXPOSE 7860

# Command to run the application
CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "src.api.app:app", "--bind", "0.0.0.0:7860", "--timeout", "300"]


FROM python:3.9-slim

# Set up environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=7860 \
    APP_HOME=/app \
    MODEL_CACHE_DIR=/app/models

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

# Create user with ID 1000 BEFORE copying files
RUN useradd -m -u 1000 user

# Create directories and set permissions
RUN mkdir -p /app/models && chown -R user:user /app

# Switch to user
USER user
ENV PATH=/home/user/.local/bin:$PATH

# Copy the rest of the application
# Note: --chown=user:user ensures files are owned by the user
COPY --chown=user:user . .

# Expose the default Hugging Face port
EXPOSE 7860

# Command to run the application
CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "src.api.app:app", "--bind", "0.0.0.0:7860", "--timeout", "300"]

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=app.settings
ENV STATIC_ROOT=/app/staticfiles
ENV DATABASE_HOST=db
ENV DATABASE_NAME=happy_driver
ENV DATABASE_USER=admn
ENV DATABASE_PASSWORD=admn
ENV DATABASE_PORT=5432

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir Django==5.1.5 pillow==11.1.0 gunicorn==21.2.0 psycopg2-binary==2.9.9 requests python-dotenv whitenoise

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create necessary directories
RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/media

# Copy project
COPY . /app/

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Run the script
CMD ["/app/entrypoint.sh"]

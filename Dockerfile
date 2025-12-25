# -----------------------------
# Base image
# -----------------------------
FROM python:3.10-slim

# -----------------------------
# Environment variables
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# -----------------------------
# Working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# System dependencies
# (needed for statsmodels, arch, matplotlib)
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    gfortran \
    liblapack-dev \
    libblas-dev \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Install Poetry
# -----------------------------
RUN pip install --no-cache-dir poetry

# -----------------------------
# Copy Poetry configuration
# (dependency layer cached by Docker)
# -----------------------------
COPY pyproject.toml poetry.lock* /app/

# -----------------------------
# Install Python dependencies
# -----------------------------
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# -----------------------------
# Copy project source code
# -----------------------------
COPY src/ /app/src/
COPY data/ /app/data/
COPY shared/ /app/shared/

# -----------------------------
# Default command
# (overridden by docker-compose)
# -----------------------------
CMD ["python", "src/main.py"]

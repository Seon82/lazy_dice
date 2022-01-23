FROM python:3.9-slim-buster

WORKDIR /app

# Install poetry:
RUN pip install poetry

# Copy in the config files:
COPY pyproject.toml poetry.lock ./
# Install only dependencies:
RUN poetry install --no-root --no-dev

# Copy in everything else and install:
COPY . .
RUN poetry install --no-dev
CMD poetry run python lazy_dice/main.py
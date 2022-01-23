FROM python:3.9

WORKDIR /home

# poetry is used to manage dependencies
RUN pip install poetry

# Copy only requirements for docker cache
COPY pyproject.toml ./
COPY poetry.lock ./

# Install globally instead of in a venv
RUN poetry config virtualenvs.create false
# Install deps
RUN poetry install  --no-dev --no-interaction


COPY lazy_dice ./lazy_dice
# COPY pipelines ./pipelines

CMD python lazy_dice/main.py
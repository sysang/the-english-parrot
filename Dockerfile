# Pull SDK image as base image
FROM rasa/rasa:2.5.1-full

# Use subdirectory as working directory
WORKDIR /app

# Change to root user to install dependencies
USER root

# Copy actions code to working directory
COPY ./modules /app/modules
# COPY ./poetry.lock /app/poetry.lock
COPY ./pyproject.toml /app/pyproject.toml

CMD ["/bin/bash"]

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Don't use root user to run code
USER 1001

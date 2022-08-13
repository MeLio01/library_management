FROM python:3.8-slim-buster

WORKDIR /library_management

COPY . /library_management

RUN pip install poetry
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN poetry install --no-root --no-dev --no-interaction --no-ansi -vvv
RUN chmod +x start_app.sh
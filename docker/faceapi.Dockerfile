FROM python:latest
LABEL maintainer="mypaceshun@gmail.com"

WORKDIR /srv

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y cmake
RUN python3 -m pip install poetry
RUN poetry config virtualenvs.in-project true

COPY ./pyproject.toml /srv/pyproject.toml
COPY ./poetry.lock /srv/poetry.lock
RUN poetry install

EXPOSE 8000

ENTRYPOINT []
CMD ["poetry", "run", "poe", "runserver"]

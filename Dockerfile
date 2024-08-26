FROM python:3.12

WORKDIR /backend

RUN pip install --no-cache-dir poetry

# COPY ./backend /code/backend

ENV POETRY_VERSION=1.0.5
RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH
COPY backend/poetry.lock backend/pyproject.toml /backend/
RUN poetry install --no-dev  # respects 

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
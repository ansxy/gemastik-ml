FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV PORT=$PORT

RUN pip install --upgrade pip

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./app /app
ENV PYTHONPATH "${PYTHONPATH}:/app/"
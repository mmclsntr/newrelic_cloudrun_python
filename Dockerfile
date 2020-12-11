FROM python:3.8.6-alpine

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /opt/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["newrelic-admin", "run-program", "uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

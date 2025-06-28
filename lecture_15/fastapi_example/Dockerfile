FROM python:3.13.5-bullseye

COPY app app/.

# No need to copy .env if you use docker-compose, variables come from environment
COPY .env .

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

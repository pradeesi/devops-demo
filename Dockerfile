FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app_arab_bank.py .

EXPOSE 8080
CMD ["python", "app_arab_bank.py"]
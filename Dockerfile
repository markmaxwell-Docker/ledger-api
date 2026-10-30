FROM python:3.12-slim
WORKDIR /app
COPY ledger ./ledger
CMD ["python3", "-c", "import ledger; print('ledger-api ready')"]

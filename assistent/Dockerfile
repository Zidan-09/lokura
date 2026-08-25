FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY assistent/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY assistent/ ./assistent/

CMD ["python", "assistent/app.py"]
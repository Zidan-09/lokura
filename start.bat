@echo off

call docker desktop start

docker compose up --build -d

.\.venv\Scripts\python.exe assistent\app.py
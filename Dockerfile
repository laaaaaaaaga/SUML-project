FROM python:3.10-slim

WORKDIR /app

COPY app.py app.py
COPY styles.css styles.css
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.enableCORS", "false", "--browser.serverAddress", "0.0.0.0", "--browser.gatherUsageStats", "false", "--server.port", "8080"]

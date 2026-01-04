# ---- Base Image ----
FROM python:3.12-slim

# ---- Set work directory ----
WORKDIR /app

# ---- Install dependencies ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy application code ----
COPY src/ ./src/

# ---- Expose port ----
EXPOSE 5000

# ---- Run application ----
CMD ["python", "src/app.py"]

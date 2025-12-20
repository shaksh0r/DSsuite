FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the app
CMD ["uvicorn", "DSsuite.main:app", "--host", "0.0.0.0", "--port", "8000"]

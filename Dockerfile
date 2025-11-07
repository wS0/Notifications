FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic --noinput
CMD ["gunicorn", "notifications.wsgi:application", "--bind", "0.0.0.0:8000"]
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

COPY pyproject.toml README.md ./
COPY app.py ./
COPY src ./src

RUN pip install --no-cache-dir .

EXPOSE 5000

CMD ["python", "app.py"]
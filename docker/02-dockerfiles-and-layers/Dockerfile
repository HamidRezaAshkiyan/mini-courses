FROM python:3.12-alpine

# Create a non-root user for better security
RUN adduser -D appuser

WORKDIR /app

COPY app.py .

USER appuser

EXPOSE 8000

CMD ["python3", "app.py"]

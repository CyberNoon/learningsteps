# Stage 1: Build & Dependency Resolution
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy requirements from the api/ subfolder
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Minimal Runtime
FROM python:3.11-slim
WORKDIR /app

# Security: Create non-root system account
RUN addgroup --system appgroup && adduser --system --group appuser

# Extract pre-compiled libraries and binaries from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy source code
COPY api/ ./api/

# Guarantee module visibility for application imports
ENV PYTHONPATH=/app/api:/app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--app-dir", "api", "--host", "0.0.0.0", "--port", "8000"]

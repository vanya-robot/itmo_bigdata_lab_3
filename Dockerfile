FROM python:3.9-slim AS builder

WORKDIR /app

COPY setup.py .
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .
RUN pip install .

FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app

# Устанавливаем Vault CLI и зависимости
RUN apt-get update && apt-get install -y curl unzip jq && \
    curl -O https://releases.hashicorp.com/vault/1.13.0/vault_1.13.0_linux_amd64.zip && \
    unzip vault_1.13.0_linux_amd64.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/vault && \
    rm vault_1.13.0_linux_amd64.zip

RUN chmod +x /app/scripts/get_secrets.sh

CMD ["sh", "-c", \
     "/app/scripts/get_secrets.sh && python src/scripts/init_db.py && uvicorn src.api.app:app --host 0.0.0.0 --port 8000"]
import hvac
import os
from src.config import settings

def init_vault():
    client = hvac.Client(url=settings.vault_addr, token=settings.vault_token)
    
    # Секреты берутся из переменных окружения (из .env файла)
    secrets = {
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "db": os.getenv("POSTGRES_DB"),
        "port": os.getenv("POSTGRES_PORT", "5432")
    }
    
    client.secrets.kv.v2.create_or_update_secret(
        path=settings.vault_secret_path,
        secret=secrets
    )

if __name__ == "__main__":
    init_vault()
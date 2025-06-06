import logging
from src.db.database import engine, Base
from src.config import settings
from src.exceptions import DatabaseInitError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    try:
        # Инициализируем подключение (теперь с Vault)
        #init_db_connection()
        
        logger.info(f"Initializing database on {settings.database_url}")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        raise DatabaseInitError(f"Database initialization failed: {str(e)}")

if __name__ == "__main__":
    init_db()
from pymongo import AsyncMongoClient
from logic_logs.file.logger import logger

try:
    connection = AsyncMongoClient("localhost", 27017)
    logger.info("MongoDB был успешно подключён")
except Exception as e:
    logger.error(f"Возника ошибка при подключение к MongoDB: {e}")

import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
# from commands.send_logs import CustomErrorHandler
from logic_logs.chat.log_base import CustomErrorHandler



def setup_logger(name: str = 'RII_BOT') -> logging.Logger:
    """
    Настройка логгера с ротацией файлов
    
    Параметры:
        name: имя логгера (по умолчанию 'heatmap')
    
    Возвращает:
        Настроенный экземпляр логгера
    """

    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler = RotatingFileHandler(
        filename=log_dir / f'{name}.log',
        maxBytes=500 * 1024 * 1024,  # 500 МБ
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    error_handler = CustomErrorHandler()
    logger.addHandler(error_handler)

    return logger

logger = setup_logger()
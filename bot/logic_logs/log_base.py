from bot.main import BOT


class LogBase:
    def __init__(self):
        self.bot = BOT
        self.log_chats = {
            "create_or_update_user": -1001948152320,
            "cache_update": -4112086004,
            "statistics": None, # заглушка
        }

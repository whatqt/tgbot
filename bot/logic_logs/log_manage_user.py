from .log_base import LogBase



class LogManageUser(LogBase):
    def __init__(
            self, id_user: int,
            user_name: str, id_group,
    ):
        super().__init__()
        self.id_user = id_user
        self.user_name = user_name
        self.id_group = id_group

    async def send_about_create_user(self):
        await self.bot.send_message(
        self.log_chats["create_or_update_user"],
        f'ПОльзователь зарегистрировался в базе данных\nИмя пользователя: {self.user_name}\nid пользователя: {self.id_user}\nгруппа пользователя: {self.id_group}'
        )

    async def send_about_update_user(self):
        await self.bot.send_message(
        self.log_chats["create_or_update_user"], f"""
Пользователь уже есть в базе данных 📋\nid пользователя {self.id_user} | user_name пользователя {self.user_name}
id группы пользователя был успешно обновлён на {self.id_group}✅
"""
        )
        
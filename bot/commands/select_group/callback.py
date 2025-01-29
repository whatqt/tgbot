from aiogram import types
from cache_group_users.cache_group_user import CacheGroupUsers 
from postgresql.management.manage_user import ManageUser



class CallbackButton:
    def __init__(self, text, callback_data, builder):
        self.text = text
        self.callback_data = callback_data
        self.builder = builder

    async def __call__(self):
        self.builder.add(types.InlineKeyboardButton(
            text=self.text,
            callback_data=self.callback_data)
            )

class CallbackData: 
    def __init__(
            self, callback_input: types.CallbackQuery, 
            text: str, keyboard = None
        ):
        self.callback_input = callback_input
        self.text = text
        self.keyboard = keyboard

    async def __call__(self):
        id_group  = self.callback_input.data.split('_')[1]
        await self.callback_input.message.edit_text(
            self.text,
            reply_markup=self.keyboard
        )
        manage_user = ManageUser(
            self.callback_input.from_user.id,
            self.callback_input.from_user.username,
            id_group,
        )
        
        result_call_create_user = await manage_user.create_user()
        if result_call_create_user:
            await manage_user.update_group_at_user(id_group)
        
        CacheGroupUsers.cache_group_users_dict[
            self.callback_input.from_user.id
        ] = f"schedule_{id_group}"
        

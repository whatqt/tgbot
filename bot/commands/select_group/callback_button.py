from aiogram import types
# from postgresql.db import insert_into_table
from postgresql_copy.manage_user import ManageUser


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

class Callbackdata: 
    def __init__(self, callback_input: types.CallbackQuery, text, keyboard = None):
        self.callback_input = callback_input
        self.text = text
        self.keyboard = keyboard

    async def __call__(self, text_compared):  # text_compared - сравниваемый текст
        id_group  = self.callback_input.data.split('_')[1]
        if id_group == text_compared:
            await self.callback_input.message.edit_text(
                self.text,
                reply_markup=self.keyboard
            )
            manage_user = ManageUser(
                self.callback_input.from_user.id,
                self.callback_input.from_user.username,
                id_group
            )
            result_call_create_user = await manage_user.create_user()
            if result_call_create_user:
                await manage_user.update_group_at_user(id_group)

        #     await insert_into_table( 
        #     self.callback_input.from_user.id,
        #     self.callback_input.from_user.username,
        #     id_group
        # ) 
            

from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
import asyncio
from aiogram import Bot
from postgresql.db import *
from send_mess_by_time.time_set import *
from datetime import datetime
from handlears.week import display_the_schedule
from handlears.current_day import *
from keyboard_builder.callback_button import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from asyncpg.exceptions import *



router = Router()

user_list = []
user_list_use_command = []

async def keyboard():
    builder = InlineKeyboardBuilder()
    await CallbackButton('Изменить время', 'edit', builder)()
    return builder.as_markup()

@router.message(Command('send_class_by_time'))
async def send_class_by_time(message: types.Message, command: CommandObject):
    if command.args is None:
        if message.from_user.id in user_list:
            await message.reply('Вы уже нажали на кнопку "Изменить время". Напишите новое время для получения уведомление.')
            return
        else:
            await message.answer('Неправильный формат команды.\n\nПравильный формат команды:\n/send_class_by_time <час:минута>')
            return
    
    elif message.from_user.id in user_list:
        await message.reply('Вы уже нажали на кнопку "Изменить время". Напишите новое время для получения уведомление.')
        return
    
    else:
        try:
            user_list_use_command.append(message.from_user.id)
            set_time = Time(command.args, message.from_user.id)
            await set_time.insert_date_time()
            await message.reply(
            f'Команда выполнена успешно. Уведомление о парах придёт в {command.args}', 
            reply_markup=await keyboard()
            )
            unsuccessful_attempts = 0
            while True:
                time = datetime.now()
                real_time = f'{time.hour}:{time.minute}'
                time_from_bd = await select_time_time(message.from_user.id)
                print(f'real_time {real_time}')
                print(f'time_from_db {time_from_bd}\n')
                if time_from_bd is None:
                    print('Пользователь сменил данные')
                    unsuccessful_attempts+=1
                    print(f'unsuccessful_attempts - {unsuccessful_attempts}')
                    print('\n')
                    if unsuccessful_attempts == 2:
                        user_list.remove(message.from_user.id)
                        await message.reply('Время для изменение времени уведомление прошло. Запустите команду еще раз.')
                        break

                    await asyncio.sleep(30)

                elif time_from_bd is not None:
                    unsuccessful_attempts = 0
                    if real_time == time_from_bd:
                        current_day = CurrentDay()
                        await delete_date_time(message.from_user.id)
                        await display_the_schedule(message.from_user.id, message.reply, await current_day_two(await current_day()))
                        user_list_use_command.remove(message.from_user.id)
                        print(f'Сеанс {message.from_user.id} закончен')
                        break

                await asyncio.sleep(30)
                    
        except KeyError:
            await message.reply('В воскресенье пар нет!')
            await delete_date_time(message.from_user.id)

        except UniqueViolationError:
            await message.reply(
                f'У вас уже установлено уведомление на {await select_time_time(message.from_user.id)}', 
                reply_markup= await keyboard()
                )
            
        except (DatetimeFieldOverflowError, InvalidDatetimeFormatError, ValueError):
            await message.reply(f'{command.args} является недопустимым значением.\nПример команды: /send_class_by_time 9:30')
    
    
@router.callback_query(F.data == 'edit')
async def edit(callback: types.CallbackQuery):
    if callback.from_user.id in user_list_use_command:
        await delete_date_time(callback.from_user.id)
        user_list.append(callback.from_user.id)
        print(f'{user_list}\n')
        await callback.message.edit_text('Напишите новое время для отправки уведомление') 
        await callback.answer()   
        @router.message()
        async def func(message: types.Message):
            try:
                if message.from_user.id in user_list:
                    set_time = Time(message.text, message.from_user.id)
                    await set_time.insert_date_time()
                    await message.reply(f'Новое время {message.text} было установлено!')
                    user_list.remove(message.from_user.id)
                    print(user_list)
                else: pass
            except (ValueError, DatetimeFieldOverflowError, InvalidDatetimeFormatError):
                await message.reply(f'{message.text} является недопустимым значением. Уведомление не было обновлено.\nПример записи времени: 21:30 ')
    else:
        await callback.message.reply(f'Вы не можете изменить время, без предварительного использование команды /send_class_by_time')


#1 если пользователь ввёл команду еще раз, то его предупреждают о том, что старая напоминалка перезапишется. Придётся настроить удаление информации с бд
#2 в дальнейшем сделать так, чтобы можно было добавлять больше уведомлений.
#3 сделать при помощи калбек кнопек так, что пользователь мог изменить время получения уведомления.
#4 сделать команду, которая будет показывать активные уведомления.
#5 можно сделать так, чтобы данные хранились в списке и этот список обновлялся
#5 и при помоще него можно было изменять или удалять выбранные уведолмения (или не в списке, а в словаре)
#6 изменить в cache current_dict, чтобы не было исключение KeyError 
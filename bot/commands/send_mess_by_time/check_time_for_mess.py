from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram import types
import asyncio
from aiogram import Bot
# from postgresql.db import *
from postgresql_copy.send_mess_by_time.send_mess_time import ManageSendMessTime
from postgresql_copy.send_mess_by_time.time_set import ManageTime
from commands.select_group.callback_button import CallbackButton
from .time_set import Time
from datetime import datetime
from lesson.week import display_the_schedule
from lesson.current_day import CurrentDay
from lesson.score_week import check_week
from .keyboard_builder.callback_button import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.exc import IntegrityError
from asyncpg.exceptions import *
from lesson.score_week import CurrentDay
import os
from dotenv import load_dotenv



load_dotenv()
router = Router()
bot = Bot(token=os.getenv('TOKEN_BOT'))

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
            # set_time = Time(command.args, message.from_user.id)
            # await set_time.insert_date_time() # из бд
            manage_time = ManageTime(command.args)
            time_from_db = await manage_time.date()
            manage_send_mess_time = ManageSendMessTime(
                message.from_user.id
            )
            await manage_send_mess_time.insert_time(
                time_from_db
            )
            unsuccessful_attempts = 0           
            await message.reply(
            f'Команда выполнена успешно. Уведомление о парах придёт в {command.args}', 
            reply_markup=await keyboard()
            )
            while True:
                new_time = datetime.now()
                real_time = f'{new_time.hour}:{new_time.minute}'
                # time_from_db_str = await select_time_str(message.from_user.id)
                print(f'real_time {real_time}')
                print(f'time_from_db {time_from_db}\n')
                if message.from_user.id in user_list:
                    print('Пользователь сменил данные')
                    unsuccessful_attempts+=1
                    print(f'unsuccessful_attempts - {unsuccessful_attempts}')
                    print('\n')
                    if unsuccessful_attempts == 2:
                        user_list.remove(message.from_user.id)
                        await message.reply('Время для изменение времени уведомление прошло. Запустите команду еще раз.')
                        break
                    
                elif user_list:
                    unsuccessful_attempts = 0
                    if real_time == str(time_from_db).split(' ')[1]:
                        current_day = CurrentDay()
                        await manage_send_mess_time.delete_time()
                        print("УДАЛЯЕМ ВРЕМЯ")
                        await display_the_schedule(message.from_user.id, message, await check_week(await current_day.today_day_week()), 'answer')
                        user_list_use_command.remove(message.from_user.id)
                        print(f'Сеанс {message.from_user.id} закончен')
                        break  

                await asyncio.sleep(30)
                
        except KeyError:
            await message.reply('В воскресенье пар нет!')
            await manage_send_mess_time.delete_time()
             

        # except IntegrityError:
        #     time_db = await manage_send_mess_time.return_time_by_id()
        #     await message.reply(
        #         f'У вас уже установлено уведомление на {time_db}', 
        #         reply_markup= await keyboard()
        #         )
            
        except (DatetimeFieldOverflowError, InvalidDatetimeFormatError, ValueError):
            await message.reply(f'{command.args} является недопустимым значением.\nПример команды: /send_class_by_time 9:30')


@router.callback_query(F.data == 'edit')
async def edit(callback: types.CallbackQuery):
    if callback.from_user.id in user_list_use_command:
        manage_send_mess_time = ManageSendMessTime(
            callback.from_user.id
        )

        await manage_send_mess_time.delete_time()
        user_list.append(callback.from_user.id)
        print(f'{user_list}\n')
        await callback.message.edit_text('Напишите новое время для отправки уведомление') 
        await callback.answer()  
        @router.message()
        async def func(message: types.Message):
            try:
                if message.from_user.id in user_list:
                    # set_time = Time(message.text, message.from_user.id)
                    # await set_time.insert_date_time()
                    set_time = ManageTime(
                        message.text
                    )
                    manage_send_mess_time = ManageSendMessTime(
                        callback.from_user.id,
                    )
                    await manage_send_mess_time.insert_time(
                        await set_time.date()
                    )
                    await message.reply(f'Новое время для уведомление {message.text} было установлено!')
                    user_list.remove(message.from_user.id)
                    print(user_list)
                else: pass

            except (ValueError, DatetimeFieldOverflowError, InvalidDatetimeFormatError):
                await message.reply(f'{message.text} является недопустимым значением. Уведомление не было обновлено.\nПример записи времени: 21:30 ')
    else:
        await callback.message.reply(f'Вы не можете изменить время, без предварительного использование команды /send_class_by_time')
        await callback.answer()

async def update_task_code(message: types.Message, id_user):
    while True:
        try:
            manage_send_mess_time = ManageSendMessTime(id_user)
            user_list_use_command.append(int(id_user))
            time = datetime.now()
            real_time = f'{time.hour}:{time.minute}'
            time_from_bd = await manage_send_mess_time.return_time_by_id()
            print(f'real_time {real_time}')
            print(f'time_from_db {time_from_bd}\n')
            if time_from_bd is None:
                print('Пользователь сменил данные')
                unsuccessful_attempts+=1
                print(f'unsuccessful_attempts - {unsuccessful_attempts}')
                print('\n')
                if unsuccessful_attempts == 2:
                    user_list.remove(message.from_user.id)
                    await bot.send_message(id_user,'Время для изменение времени уведомление прошло. Запустите команду еще раз.')
                    break
 
            elif time_from_bd:
                unsuccessful_attempts = 0
                if real_time == time_from_bd:
                    current_day = CurrentDay()
                    await manage_send_mess_time.delete_time()
                    await display_the_schedule(id_user, None, await check_week(await current_day.today_day_week()), 'bot_send')
                    user_list_use_command.remove(id_user)
                    print(f'Сеанс {id_user} закончен')
                    break
            
            await asyncio.sleep(30)
            
        except KeyError:
            await bot.send_message(id_user, 'В воскресенье пар нет!')
            await manage_send_mess_time.delete_time()
            break
            
@router.message(Command('update_task'))
async def update_task(message: types.Message):
    if message.from_user.id == 1752086646:
        manage_send_mess_time = ManageSendMessTime(...)
        result_db = await manage_send_mess_time.return_all_user()
        tasks = []
        for info_db in result_db:
            id_user = str(info_db).split('id_user=')[1].split(maxsplit=1)[0].replace('>', '')
            print(id_user)
            task = asyncio.create_task(update_task_code(message, int(id_user)))
            tasks.append(task)
        await asyncio.gather(*tasks)
    else: pass
    

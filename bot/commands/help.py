from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


router = Router()

@router.message(Command('help'))
async def help(message: types.Message):
    await message.reply(
'''
/group - позволяет выбрать курс и группу.\n
/schedule - создаёт кнопку "Расписание пар".\n
/send_class_by_time - позволяет отправить актуальное расписание через установленное вами время.
Примеры команды: 
/send_class_by_time 9:30
/send_class_by_time 21:30\n
/feedback - команда позволяет написать отзыв о боте. Здесь можете написать его недостатки, что хотели бы добавить сюда, и различные советы.
Пример команды: /feedback <ваш комментарий>.\n
/report - позволяет сообщить об ошибке в боте.
Пример команды: /report <ваш отчёт об ошибке>.\n
Писать по вопросам @what_whatqwe\n 
Автор бота: @what_whatqwe\n
Соавтор: @belomaxorka
'''
    )

@router.message(Command('support'))
async def support(message: types.Message):
   await message.reply('Если возник вопрос, то пишите сюда: @what_whatqwe')
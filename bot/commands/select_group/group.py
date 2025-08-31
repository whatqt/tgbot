from aiogram import Router, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .callback import CallbackButton, CallbackData
from aiogram import types
from .groups import first_course, second_course, third_course, fourth_course
from commands.schedule import create_schedule



router = Router()

async def course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("Первый курс", "first_course", builder)(),
    await CallbackButton("Второй курс", "second_course", builder )(), # вызов объекта класса как функции
    await CallbackButton("Третий курс", "third_course", builder)(),
    await CallbackButton("Четвёртый курс", "fourth_course", builder)(),
    builder.adjust(2)
    return builder.as_markup()

async def get_first_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-51", "firstcourse_1027", builder)(),
    await CallbackButton("ИСП11-51", "firstcourse_1039", builder)(),
    await CallbackButton("ИСП9-51", "firstcourse_1035", builder)(),
    await CallbackButton("ИСП9-52", "firstcourse_1038", builder)(),
    await CallbackButton("КТМ-51", "firstcourse_1028", builder)(),
    await CallbackButton("С-51", "firstcourse_1029", builder)(),
    await CallbackButton("ЭБУ9-51", "firstcourse_1032", builder)(), 
    await CallbackButton("ЭиЭ-51", "firstcourse_1030", builder)()
    await CallbackButton("ЭиЭ-52", "firstcourse_1031", builder)()
    await CallbackButton("ЭС11-51", "firstcourse_1036", builder)()
    await CallbackButton("ЭС9-51", "firstcourse_1037", builder)()
    await CallbackButton("Выбрать другой курс", "firstcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()

async def get_second_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-41", "secondcourse_1016", builder)(),
    await CallbackButton("ИСП9-41", "secondcourse_1020", builder)(),
    await CallbackButton("ИСП9-42", "secondcourse_1021", builder)(),
    await CallbackButton("КТМ-41", "secondcourse_1017", builder)(),
    await CallbackButton("С-41", "secondcourse_1018", builder)(),
    await CallbackButton("ЭБУ9-41", "secondcourse_1025", builder)(),
    await CallbackButton("ЭиЭ-41", "secondcourse_1019", builder)(), 
    await CallbackButton("ЭС11-41", "secondcourse_1024", builder)()

    await CallbackButton("Выбрать другой курс", "secondcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()

async def get_third_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИСП9-31", "thirdcourse_1008", builder)()
    await CallbackButton("ИСП9-32", "thirdcourse_1014", builder)()
    await CallbackButton("ЭБУ9-31", "thirdcourse_1010", builder)()
    await CallbackButton("КТМ-31", "thirdcourse_1005", builder)()
    await CallbackButton("С-31", "thirdcourse_1006", builder)()
    await CallbackButton("ЭиЭ-31", "thirdcourse_1007", builder)()
    await CallbackButton("ЭС11-31", "thirdcourse_1013", builder)()
    await CallbackButton("ИВТ-31", "thirdcourse_1004", builder)()
    await CallbackButton("ИСП11-31", "thirdcourse_1009", builder)()
    await CallbackButton("Выбрать другой курс", "thirdcourse_back", builder)()
    builder.adjust(4)
    return builder.as_markup()

async def get_fourth_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-21", "fourthcourse_992", builder)()
    await CallbackButton("ИСП9-21", "fourthcourse_988", builder)()
    await CallbackButton("КТМ-21", "fourthcourse_994", builder)()
    await CallbackButton("С-21", "fourthcourse_991", builder)()
    await CallbackButton("ЭиЭ-21", "fourthcourse_993", builder)()
    await CallbackButton("Выбрать другой курс", "fourthcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()

@router.message(Command('group'))
async def group(message : types.Message):
    await message.answer('Выберите группу', reply_markup=await course())

@router.callback_query(F.data.endswith("course"))
async def callback_group(callback : types.CallbackQuery):
    data = callback.data.split('_')[0]
    if data == 'first':
        await callback.message.edit_text('Группы первого курса', reply_markup= await get_first_course())
    elif data == 'second':
        await callback.message.edit_text('Группы второго курса', reply_markup= await get_second_course())
    elif data == 'third':
        await callback.message.edit_text('Группы третьего курса', reply_markup= await get_third_course())
    elif data == 'fourth':    
        await callback.message.edit_text('Группы четвёртого курса', reply_markup= await get_fourth_course())
    await callback.answer()

@router.callback_query(F.data.startswith("firstcourse"))
async def callback_group(callback: types.CallbackQuery):
    result_data = callback.data.split('_')[1]
    if result_data in first_course:
        await CallbackData(callback, f'✅ {first_course[result_data]}', await course())()
        await create_schedule(callback)
    elif result_data == "back":
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()

@router.callback_query(F.data.startswith("secondcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in second_course:
        await CallbackData(callback, f'✅ {second_course[result_data]}', await course())()
        await create_schedule(callback)

    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()

@router.callback_query(F.data.startswith("thirdcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in third_course:
        await CallbackData(callback, f'✅ {third_course[result_data]}', await course())()
        await create_schedule(callback)
    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()

@router.callback_query(F.data.startswith("fourthcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in fourth_course:
        await CallbackData(callback, f'✅ {fourth_course[result_data]}', await course())()
        await create_schedule(callback)
    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())
    await callback.answer()
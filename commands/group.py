from aiogram import Router, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboard_builder.callback_button import CallbackButton, Callbackdata
from aiogram import types
from groups.groups import first_course, second_course, third_course, fourth_course
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

async def  get_first_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИСП9-31", "firstcourse_1008", builder)(),
    await CallbackButton("ИСП9-32", "firstcourse_1014", builder)(),
    await CallbackButton("ЭБУ9-31", "firstcourse_1010", builder)(),
    await CallbackButton("КТМ-31", "firstcourse_1005", builder)(),
    await CallbackButton("С-31", "firstcourse_1006", builder)(),
    await CallbackButton("ЭБУ11-31", "firstcourse_1011", builder)(),
    await CallbackButton("ЭиЭ-31", "firstcourse_1007", builder)(),
    await CallbackButton("ЭС11-31", "firstcourse_1013", builder)(),
    await CallbackButton("ИВТ-31", "firstcourse_1004", builder)(), 
    await CallbackButton("ИСП11-31", "firstcourse_1009", builder)()
    await CallbackButton("Выбрать другой курс", "firstcourse_back", builder)()
    builder.adjust(3)
    return builder.as_markup()

async def get_second_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-21", "secondcourse_992", builder)(),
    await CallbackButton("ИСП11-21", "secondcourse_987", builder)(),
    await CallbackButton("ИСП9-21", "secondcourse_988", builder)(),
    await CallbackButton("КТМ-21", "secondcourse_994", builder)(),
    await CallbackButton("С-21", "secondcourse_991", builder)(),
    await CallbackButton("ЭБУ11-21", "secondcourse_989", builder)(),
    await CallbackButton("ЭБУ9-21", "secondcourse_990", builder)(),
    await CallbackButton("ЭиЭ-21", "secondcourse_993", builder)(),
    await CallbackButton("Выбрать другой курс", "secondcourse_back", builder)()
    builder.adjust(4)
    return builder.as_markup()

async def get_third_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИВТ-11", "thirdcourse_977", builder)(),
    await CallbackButton("ИСП-11", "thirdcourse_984", builder)(),
    await CallbackButton("КТМ-11", "thirdcourse_979", builder)(),
    await CallbackButton("С-11", "thirdcourse_976", builder)(),
    await CallbackButton("ЭБУ11-11", "thirdcourse_982", builder)(),
    await CallbackButton("ЭБУ9-11", "thirdcourse_983", builder)(),
    await CallbackButton("ЭиЭ-11", "thirdcourse_978", builder)(),
    await CallbackButton("ЭФК-11", "thirdcourse_981", builder)(),
    await CallbackButton("Выбрать другой курс", "thirdcourse_back", builder)()
    builder.adjust(4)
    return builder.as_markup()

async def get_fourth_course():
    builder = InlineKeyboardBuilder()
    await CallbackButton("ИСП9-31", "fourthcourse_937", builder)(),
    await CallbackButton("ИСП9-32", "fourthcourse_940", builder)(),
    await CallbackButton("ЭБУ9-31", "fourthcourse_936", builder)(),
    await CallbackButton("КТМ-31", "fourthcourse_919", builder)(),
    await CallbackButton("С-31", "fourthcourse_933", builder)(),
    await CallbackButton("Выбрать другой курс", "thirdcourse_back", builder)()
    builder.adjust(5)
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
        await Callbackdata(callback, f'✅ {first_course[result_data]}', await course())(result_data)
        await create_schedule(callback)
    elif result_data == "back":
        await callback.message.edit_text('Выберите группу', reply_markup= await course())

    await callback.answer()

@router.callback_query(F.data.startswith("secondcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in second_course:
        await Callbackdata(callback, f'✅ {second_course[result_data]}', await course())(result_data)
        await create_schedule(callback)

    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())

    await callback.answer()

@router.callback_query(F.data.startswith("thirdcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in third_course:
        await Callbackdata(callback, f'✅ {third_course[result_data]}', await course())(result_data)
        await create_schedule(callback)
    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())

    await callback.answer()

@router.callback_query(F.data.startswith("fourthcourse"))
async def callback_group(callback: types.CallbackQuery,):
    result_data = callback.data.split('_')[1]
    if result_data in fourth_course:
        await Callbackdata(callback, f'✅ {fourth_course[result_data]}', await course())(result_data)
        await create_schedule(callback)
    else:
        await callback.message.edit_text('Выберите группу', reply_markup= await course())

    await callback.answer()
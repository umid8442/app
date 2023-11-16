from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp
from keyboards.default.murcap import settings, questions, orders, delivery_status
from keyboards.default.murcap import catalog, balance, cart
from filters import IsUser, IsAdmin


@dp.message_handler(IsAdmin(), commands=['menu'])
async def admin_menu(message: Message):
    murcap = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    murcap.add(settings)
    murcap.row(questions, orders)

    await message.answer(text='Menu',
                         reply_markup=murcap)


@dp.message_handler(IsUser(), commands=['menu'])
async def user_menu(message: Message):
    murkup = ReplyKeyboardMarkup
    murkup.add(catalog)
    murkup.row(balance, cart)
    murkup.add(delivery_status)

    await message.answer(text='menu',
                         reply_markup=murkup)

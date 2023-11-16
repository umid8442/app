import sqlite3

from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from keyboards.default.murcap import user_message, admin_message
from data.config import ADMINS
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    murkap = ReplyKeyboardMarkup(resize_keyboard=True)

    murkap.row(user_message, admin_message)
    await message.answer(text='''Привет! 👋

🤖 Я бот-магазин по подаже товаров любой категории.
    
🛍 Чтобы перейти в каталог и выбрать приглянувшиеся товары возпользуйтесь командой /menu.

💰 Пополнить счет можно через Яндекс.кассу, Сбербанк или Qiwi.

❓ Возникли вопросы? Не проблема! Команда /sos поможет связаться с админами, которые постараются как можно быстрее откликнуться.

🤝 Заказать похожего бота? Свяжитесь с разработчиком  <a href="https://t.me/fozilovbekzod">Bekzod</a>
     ''', reply_markup=murkap,
                         disable_web_page_preview=True)


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):
    cid = message.chat.id
    if cid in ADMINS:
        ADMINS.remove(cid)
    await message.answer(text='foydalanuvhi rejimi yoqildi.',
                         reply_markup=ReplyKeyboardMarkup())


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):
    cid = message.chat.id
    if cid not in ADMINS:
        ADMINS.remove(cid)

    await message.answer(text='admin rejim yoqildi..',
                         reply_markup=ReplyKeyboardRemove())


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import dp

category_cp = CallbackData('category', 'id', 'action')


def categories_murcap():
    global category_cp

    murkap = InlineKeyboardMarkup()
    for idx, title in dp.select_catigories_fatchall():
        murkap.add(InlineKeyboardButton(title, callback_data=category_cp.new(id=idx,
                                                                             action='view')))
        return murkap

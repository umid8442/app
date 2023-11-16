from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

product_cb = CallbackData('product', 'id', 'action')


def product_murkap(idx='', price=0):
    global product_cb

    murkap = InlineKeyboardMarkup()
    murkap.add(InlineKeyboardButton(f'karzinaga qoshiw - {price}',
                                    callback_data=product_cb.new(id=idx, action='add')))

    return murkap
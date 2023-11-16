from aiogram.types import Message, CallbackQuery
from aiogram.types.chat import ChatActions
from keyboards.default.murcap import catalog
from keyboards.inline.catigories import categories_murcap, category_cp
from keyboards.inline.products_from_catalog import product_cb, product_murkap
from filters import IsUser
from loader import dp, db, bot


@dp.message_handler(IsUser(), text=catalog)
async def process_catalog(message: Message):
    await message.answer(text='tavar spiskasi chiqiwi uchun ,bolimni tanlang',
                         reply_markup=categories_murcap())


@dp.callback_query_handler(IsUser(), category_cp.filter(action='view'))
async def category_callback_handler(query: CallbackQuery, callback_data: dict):
    product = dp.select_products_in_categories(callback_data['id'], query.message.chat.id)
    await query.answer('hamma tavarlar')
    await show_product(query.message, product)


@dp.callback_query_handler(IsUser(), product_cb.filter(action='add'))
async def add_product_callback_handler(query: CallbackQuery, callback_data: dict):
    db.interp_intro_card((query.message.chat.id, callback_data['id']))
    await query.answer('tavar savatga qowildi')
    await query.message.delete()


async def show_product(message, product):
    if len(product) == 0:
        await message.answer('xech narsa topilmadi')
    else:
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)

        for idx, title, body, imag, price, _ in product:
            murkap = product_murkap(idx, price)
            text = f'<b>{title}</b>\n\n{body}'
            await message.answer_photo(photo=imag,
                                       caption=text,
                                       reply_markup=murkap)

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.inline.buy_book import book_keys
from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("kitob"))
async def send_book(message: types.Message):
    photo_id = "https://i.pinimg.com/originals/72/65/ef/7265efeaa34d381d31382a75aaa03411.jpg"
    msg = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n"
    msg += "Narxi: 50000 so'm\n\n"
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)


@dp.message_handler(Command("kurslar"))
async def send_courses(message: types.Message):
    album = types.MediaGroup()
    photo1 = "https://cdn1.ozone.ru/s3/multimedia-e/6017065274.jpg"
    album.attach_photo(photo=photo1, caption='kurslar')
    await message.reply_media_group(media=album)

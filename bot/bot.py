import os
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.enums import ContentType
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.markdown import hbold
from aiogram.utils.chat_action import ChatActionSender
from aiogram import F
from messages import START_MESSAGE, HELP_MESSAGE
import asyncio
import numpy as np
import requests


TOKEN = "7744437376:AAH6-SVyzpL6KOkVfju6OmlJeE9gKjmVszY"
router = Router()


async def on_startup():
    pass


@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(START_MESSAGE)


@router.message(F.photo)
async def predict_photo(message: Message, bot: Bot):
    await message.answer("📷 Получено фото. Обрабатываю...")

    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = f"images/{photo.file_id}.jpg"
    os.makedirs("images", exist_ok=True)
    await bot.download_file(file.file_path, destination=file_path)
    with open(file_path, 'rb') as f:
        files = {'file': f}
        respone = requests.post("http://127.0.0.1:8000/predict", files=files)
    predict = respone.json()["prediction"]

    await message.answer(f"🧠 Я думаю, это стиль: {predict}")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

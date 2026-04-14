import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Кнопки серверов ---
servers_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Las Vegas"), KeyboardButton(text="Los Angeles")],
        [KeyboardButton(text="Detroit"), KeyboardButton(text="Washington")],
        [KeyboardButton(text="New York"), KeyboardButton(text="Dallas")],
        [KeyboardButton(text="Boston"), KeyboardButton(text="Houston")],
        [KeyboardButton(text="Miami"), KeyboardButton(text="San Francisco")],
        [KeyboardButton(text="San Diego"), KeyboardButton(text="Seattle")],
        [KeyboardButton(text="Denver"), KeyboardButton(text="Phoenix")],
        [KeyboardButton(text="Portland"), KeyboardButton(text="Orlando")],
    ],
    resize_keyboard=True
)

# --- Кнопки награды ---
reward_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Вирты"), KeyboardButton(text="🪙 Majestic Coins")]
    ],
    resize_keyboard=True
)

# --- Старт ---
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выбери сервер:", reply_markup=servers_kb)

# --- Обработка ---
@dp.message()
async def handler(message: types.Message):
    servers = [
        "Las Vegas","Los Angeles","Detroit","Washington",
        "New York","Dallas","Boston","Houston",
        "Miami","San Francisco","San Diego","Seattle",
        "Denver","Phoenix","Portland","Orlando"
    ]

    if message.text in servers:
        await message.answer(
            f"Ты выбрал сервер: {message.text}\n\nВыбери награду:",
            reply_markup=reward_kb
        )

    elif message.text == "💰 Вирты":
        await message.answer("Введи логин для получения виртов:")

    elif message.text == "🪙 Majestic Coins":
        await message.answer("Введи логин для получения Majestic Coins:")

    else:
        await message.answer("Используй кнопки ниже 👇")

# --- Запуск ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

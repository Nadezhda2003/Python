from aiogram import types
async def start(message: types.Message):
    await message.answer("Привет!\nНапиши мне что-нибудь!")
async def echo(message: types.Message):
    await message.answer("Сам ты: " + message.text)
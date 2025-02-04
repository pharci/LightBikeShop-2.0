from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards.keyboards import autokey

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    
    await message.answer(
        f"Добро пожаловать! Я ваш бот.", 
        reply_markup=autokey({'Заказы': 'Orders'})
        )
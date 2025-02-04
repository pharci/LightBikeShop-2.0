from aiogram import Router, types
from bot.keyboards import *
from aiogram import F, Router
from bot.keyboards.keyboards import autokey

router = Router()

@router.callback_query(F.data == "Orders")
async def start(call: types.CallbackQuery):
    await call.message.edit_text("Ваши заказы", reply_markup=autokey({'Назад': 'start'}))
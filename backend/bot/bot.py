from aiogram import Bot, Dispatcher
import os
from aiogram.fsm.storage.memory import MemoryStorage

from .handlers.callbacks.order import router as r_ord
from .handlers.commands.start import router as r_st

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_router(r_ord)
dp.include_router(r_st)
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN_API

storage = MemoryStorage()
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
    await message.text("Добро пожаловать", reply_markup=)

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True
    )
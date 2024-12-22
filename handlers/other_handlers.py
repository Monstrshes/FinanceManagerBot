from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import lexicon_ru

router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def process_other_message(message: Message):
    await message.answer(
        text=lexicon_ru["error_message"]
    )
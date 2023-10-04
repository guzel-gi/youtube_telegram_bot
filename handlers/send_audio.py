import logging
from utils import download, remove
from utils.audio_functions import get_audio_size
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile

logging.basicConfig(filename='logs.log', level=logging.ERROR)

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Укажите ссылку на видео.')

@router.message()
async def send_audio_file(message: Message):
    try:
        info = download.download_audio(message.text)
        audio_file = FSInputFile(info['file_path'])
        await message.answer_voice(voice=audio_file, caption=info['title'])
        remove.remove_file(info['file_path'])
    except Exception:
        logging.error(Exception, exc_info=True)
        await message.answer('Ничего не нашел. Проверьте правильность ссылки')
    
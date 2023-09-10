from utils import download, remove
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Укажите ссылку на видео.')

@router.message()
async def send_audio_file(message: Message):
    try:
        file_path = download.download_video(message.text)
        audio_file = FSInputFile(file_path)
        await message.answer_voice(audio_file)
        remove.remove_file(file_path)
    except:
        await message.answer('Ничего не нашел. Проверьте правильность ссылки')
    
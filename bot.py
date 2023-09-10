import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from handlers.send_audio import router

logging.basicConfig(filename='logs.log', level=logging.ERROR)

async def main():
    token = os.getenv('token')
    if token is None:
        logging.error('Токен не указан')

    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

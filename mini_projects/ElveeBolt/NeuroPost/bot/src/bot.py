import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.triggers.interval import IntervalTrigger

from config import settings
from scheduler import scheduler
from tasks.publish_posts import publish_posts

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=settings.token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)

dp = Dispatcher()


async def main():
    scheduler.add_job(
        publish_posts, IntervalTrigger(seconds=settings.post_interval), args=(bot,)
    )
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

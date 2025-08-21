from aiogram import Bot

from src.services.project import get_posts, update_post_publish_status


async def publish_posts(bot: Bot):
    posts = await get_posts()
    if posts:
        for post in posts:
            channel = post.plan.project.channel
            message = f"*{post.title}*\n\n{post.description}"

            try:
                await bot.send_message(chat_id=channel, text=message)
                await update_post_publish_status(post_id=post.id)
            except Exception as e:
                print(e)

import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["پەخشکردن لە کەناڵ","پەخشکردن لە کەنال"])
    & filters.group
)
async def khlop(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/31a48bd8769b47d9b2db8.mp4",
        caption=f"""**• دوگمەی خوارەوە دابگرە بۆ فێرکاری پەخشکردنی گۆرانی لە کەناڵ •**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/EHS4SS"),
                ],[
                    InlineKeyboardButton(
                        "فێرکاری پەخشکردن لە کەناڵ", callback_data=f"cha"),
                ],
            ]
        ),
    )

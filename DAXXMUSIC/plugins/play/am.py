import asyncio
from pyrogram import Client, filters
from config import BANNED_USERS
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



@app.on_message(
    command("ئەلینا")
    & filters.group
    & ~BANNED_USERS
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/0a648eba9c9163765c265.mp4",
        caption=f"""**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا (:\n\n- فەرمانەکان بە دوگمەن فێریان بە\n\n• 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 -› [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅](t.me/IQ7amo)\n• 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂](t.me/MGIMT)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "فێرکاری پەخشکردن لە پلاتفۆڕمەکان", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "فەرمانی گرووپ", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "فەرمانی کەناڵ", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "گرێدانی کەناڵ", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "فەرمانی گەڕان", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "فەرمانی خزمەتگوزاری", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        "نوێکارییەکانی ئەلینا 🥢", url=f"https://t.me/MGIMT"),
                ],
            ]
        ),
    )

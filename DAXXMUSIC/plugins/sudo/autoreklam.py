import asyncio
import datetime
from DAXXMUSIC import app
from pyrogram import Client
from DAXXMUSIC.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"""**چەناڵێک تایبەت بە وتە و ڤیدیۆی بێ لۆگۆ 🌚🖤!

هەرئێستا جۆینی بکە پەشیمان نابیەوە [”﮼احساس“ 🖤!](t.me/EHS4SS)

بۆتێکی گۆرانی شاز و بێ حەل
➥ پشتگێری - تێبینی لێفت، تاگ کردن، باند - میوت، داگرتنی ڤیدیۆ و گۆرانی، ڤیدیۆی تیك تۆك ...

➲ بۆتی جۆین » [𝑰𝑸 𝑱𝑶𝑰𝑵 𝑩𝑶𝑻](t.me/IQJOBOT)

➲ بۆتی گۆرانی » [𝙄𝙌 𝙈𝙐𝙎𝙄𝘾 ♥️•](t.me/IQMCBOT)
**"""

BUTTON = reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تێکستی بچووك 🫧🖤»", url=f"https://t.me/EHS4SS"),
                    InlineKeyboardButton(
                        "وتەی ئاشقانە 🫧🖤»", url=f"https://t.me/EHS4SS"),
                 ],[
                    
                
                    InlineKeyboardButton(
                        "بۆتی گۆرانی", url=f"https://t.me/IQMCBOT"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "بۆتی جۆین", url=f"https://t.me/IQJOBOT"),
                    InlineKeyboardButton(
                        "جۆینی کەناڵ بکە 🫧🖤»", url=f"https://t.me/EHS4SS"),
                
                ],[
                    
                
                    InlineKeyboardButton(
                        "زیادم بکە گرووپت", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"),
                ],

            ]

        ),

    )


async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo="", caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)  # Sleep for 1 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats
async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(30000)  # Sleep (30000 seconds) between next broadcast

# Start the continuous broadcast loop
asyncio.create_task(continuous_broadcast())

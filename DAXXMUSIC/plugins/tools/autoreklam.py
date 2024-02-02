import asyncio
import datetime
from DAXXMUSIC import app
from pyrogram import Client
from DAXXMUSIC.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MESSAGE = f"""**
➲چەناڵێک تایبەت بە وتە و ڤیدیۆی بێ لۆگۆ 🌚🖤!

➲ هەرئێستا جۆینی بکە پەشیمان نابیەوە [وتەھ 🖤](t.me/wtay_jw4n)

➲ لینکی کەناڵ 
https://t.me/Wtay_jw4n
**"""

BUTTON = reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "تێکستی بچووك 🫧🖤»", url=f"https://t.me/Wtay_jw4n"),
                      InlineKeyboardButton(
                        "وتەی ئاشقانە 🫧🖤»", url=f"https://t.me/Wtay_jw4n"),
                ],[
                      InlineKeyboardButton(
                        "جۆینی کەناڵ بکە 🫧🖤»", url=f"https://t.me/Wtay_jw4n")
                ],[
                       InlineKeyboardButton(
                          "وتەھ 🫧🖤»", url=f"https://t.me/Wtay_jw4n"),
                       InlineKeyboardButton(
                           "ئێرە دابگرە 🫧🖤»", url=f"https://t.me/Wtay_jw4n"),
                ],[

                        InlineKeyboardButton(
                        "بۆتی جۆین 🫧🖤»", url=f"https://t.me/iqjobot"),


                ],
            ]
        )



async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo="https://graph.org/file/a90c116b776c90d58f5e8.jpg", caption=MESSAGE, reply_markup=BUTTON)
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

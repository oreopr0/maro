import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from DAXXMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from DAXXMUSIC import app
import config
from config import BANNED_USERS
from config import OWNER_ID
from DAXXMUSIC import Telegram, YouTube, app
from DAXXMUSIC.misc import SUDOERS



@app.on_callback_query(filters.regex("ddd"))
async def dddf(_, query: CallbackQuery):
    from_user = int(data[1])
    user_id = CallbackQuery.from_user.id
    if user_id != CallbackQuery.message.reply_to_message.from_user.id:
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە!", show_alert=True)

    await query.edit_message_text(
       f"""\n\n\n**╭── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╮**\n\n **✧ فەرمانی پەخشکردن لە گرووپ**\n\n**• پلەی + ناوی گۆرانی یان ڕیپلەی لینك** \n-› بۆ پەخشکردنی گۆرانی لە گرووپ\n\n• **وەستان** یان **ڕاگرتن**\n-› بۆ وەستاندنی پەخشکردن\n\n• **سکیپ** یان **دواتر**\n-› بۆ گۆڕینی گۆرانی دواتر\n\n• **وەستانی کاتی** یان **وسبە**\n-› بۆ وەستاندنی پەخشکردن بۆ ماوەیەکی کاتی\n\n• **د** یان **دەستپێکردنەوە**\n-› بۆ دەستپێکردنەوەی پەخشکردن کاتێ وەستاوە\n\n**╰── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╯""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "”﮼احساس“", url=f"https://t.me/EHS4SS")
                ],[
                    InlineKeyboardButton(
                        "گەڕانەوە", callback_data="am"),
                    InlineKeyboardButton(
                        "داخستن", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data="fft"),

               ],
          ]
        ),
    )

@app.on_message(command(["کەناڵ", "کەنال"]))
def vgdg(client, message):
    message.reply_text(
       f"""**✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂\n✧ 𝑱𝒐𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑨𝒍𝒊𝒏𝒂 𝑻𝒐 𝑺𝒆𝒆 𝑨𝒍𝒍 𝑼𝒑𝒅𝒂𝒕𝒆\n\n- 𝑴𝒂𝒔𝒕𝒆𝒓 -› @IQ7amo\n- 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 -› @MGIMT**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "◌ᴅᴇᴠᴇʟᴏᴘᴇʀ◌", url=f"t.me/IQ7amo")
                ],[
                    InlineKeyboardButton(
                        "فەرمانی ئەلینا", callback_data="am"),
                    InlineKeyboardButton(
                        "”﮼احساس“", url=f"https://t.me/EHS4SS")
                ],[

                    InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data="fft"),

               ],
          ]
        ),
    )

#test
import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from DAXXMUSIC import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from DAXXMUSIC import Telegram, YouTube, app
from DAXXMUSIC.misc import SUDOERS
from DAXXMUSIC.plugins.sudo.sudoers import sudoers_list
from DAXXMUSIC.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from DAXXMUSIC.utils.decorators.language import LanguageStart
from DAXXMUSIC.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

from DAXXMUSIC import check_client


@app.on_callback_query(filters.regex("tt"))
async def gtt(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە!", show_alert=True)


    await query.edit_message_text(
       f"""\n\n**╭── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╮**\n\n** ✧ فەرمانی پەخشکردن لە کەناڵ**\n\n**• پ کەناڵ + ناوی گۆرانی یان ڕیپلەی لینك** \n-› بۆ پەخشکردنی گۆرانی لە کەناڵ\n\n**• وەستان**\n-› بۆ وەستانی هەموو گۆرانیەکان کۆتایی هاتن\n\n**• دواتر**\n-› بۆ گۆڕینی گۆرانی بۆ گۆرانی دواتر\n\n**• وەستانی کاتی**\n -› بۆ وەستانی پەخشکردن بۆ ماوەیەکی کاتی\n\n**• دەستپێکردنەوە**\n -› بۆ دەستپێکردنەوەی پەخشکردن کاتێ وەستاوە\n\n**╰── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╯**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/EHS4SS")
                ],[
                    InlineKeyboardButton(
                        "گەڕانەوە", callback_data="am"),
                    InlineKeyboardButton(
                        "داخستن", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data="kdm"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft")


               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("am"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە!", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://graph.org/file/0a648eba9c9163765c265.mp4",None,
           "**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا\n\n-هەندێك دوگمە هەن بۆ فێربوون ان شاء الله\n\n• گەشەپێدەری بۆت -› @IQ7amo\n• کەناڵی بۆت -› @MGIMT**"
       ),
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

@app.on_callback_query(filters.regex("amm"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە!", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://graph.org/file/0a648eba9c9163765c265.mp4",None,
           "**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا (:\n\n- فەرمانەکان بە دوگمەن فێریان بە\n\n• 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 -› [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅](t.me/IQ7amo)\n• 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂](t.me/MGIMT)**"
       ),
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


@app.on_callback_query(filters.regex("sound"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە!", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph/file/13308564f92131709856c.jpg",
           "**✶ بەخێربێن بۆ بەشی پەخشی ساوند کڵاود ♪**\n\n**• فەرمانی پەخشکردن بنووسە لەگەڵ لینکی ساوند کڵاود**\n\n**• نموونە :** [ `پلەی https://soundcloud.app.goo.gl/asiXLu19szSrVLFo9` ]\n\n-› [𝖲𝗈𝗎𝗇𝖽𝖢𝗅𝗈𝗎𝖽 ♪](t.me/EHS4SS)"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
   
                     InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"ko")
                ],[

                     InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft")

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("cha"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە!", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://graph.org/file/31a48bd8769b47d9b2db8.mp4",None,
           "**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا**\n**◌پەخشکردن لە کەناڵ چەند هەنگاوێکی پێویستە◌ :**\n\n1 -› بۆت زیادبکە کەناڵ و بیکە بە ئەدمین\n2 -› بگەڕێوە گرووپ و بنووسە { **گرێدان + یوزەری کەناڵ** }\n3 -› **دەست بدە لە فەرمانی پەخشکردن بۆ زانینی پەخشکردن**\n\n**✶ پەیوەندی کردن - @IQ7amo**"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "فەرمانی پەخشکردن لە کەناڵ", callback_data=f"tt"),

                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("kdm"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە!", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph/file/5306c1c651eb877f67c48.jpg",
           "✧ **اهلين فيك في قسم الاوامر الخدمية**\n-** عندك اوامر كثيرة للتسلية ومنها ↓**\n\n-› **غنيلي\n-› افتارات بنات\n-› افتارات عيال\n-› افتارات مكس\n -› هيدرات او هيدر\n-› اقتباس او اقتباسات\n-› كت**\n\n✶ **ايضا تقدر تتابع قناة ميرا فيها تشكلية كبيرة من كل الي ذكرتهم فوق**\n-› @EHS4SS"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"am"),
                ],[
                 
                     InlineKeyboardButton(
                        "• 𝑷𝒓𝒐𝒑𝒆𝒓𝒕𝒚 𝑨𝒍𝒊𝒏𝒂 •", url=f"t.me/EHS4SS")

                ],
            ]
        ),
    )

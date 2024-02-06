import asyncio
import random
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.enums import ParseMode, ChatMemberStatus
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC import app, Telegram


txt = [
    "بارده",
    "اجيت",
    "جبان",
    "مافهمت",
    # أضف المزيد من الكلمات هنا
]

correct_answers = [
    "بارده",
    "اجيت",
    "جبان",
    "مافهمت",
    # قم بإضافة الإجابات الصحيحة المطابقة للكلمات هنا
]

current_question_index = 0

app = Client("my_bot")

@app.on_message(filters.command(["كلمه"], ""))
async def game_handler(client: Client, message: Message):
    global current_question_index

    if current_question_index >= len(txt):
        await message.reply("تم انتهاء الأسئلة.")
        return

    current_question = txt[current_question_index]
    correct_answer = correct_answers[current_question_index]

    if message.text.lower() == correct_answer:
        await message.reply("إجابة صحيحة!")
        current_question_index += 1

        if current_question_index < len(txt):
            await message.reply(f"السؤال الحالي: {txt[current_question_index]}")
        else:
            await message.reply("تم انتهاء الأسئلة. شكرًا للمشاركة.")
    else:
        await message.reply("إجابة خاطئة. حاول مرة أخرى.")

app.run()
        if current_question_index < len(txt):
            await message.reply(f"السؤال الحالي: {txt[current_question_index]}")
        else:
            await message.reply("تم انتهاء الأسئلة. شكرًا للمشاركة.")
    else:
        await message.reply("إجابة خاطئة. حاول مرة أخرى.")

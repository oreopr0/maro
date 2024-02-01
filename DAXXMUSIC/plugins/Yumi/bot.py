import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AnonXMusic import app
from config import OWNER_ID
from DAXXMUSIC.misc import SUDOERS


@app.on_message(filters.command(['بوت', 'بۆت'], prefixes=""))
async def Italymusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("• زیادم بکە بۆ گرووپت 🎻", url=f"https://t.me/IQMCBOT?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == SUDOERS:
             rank = "گەشەپێدەری بۆت ⚡️"
        elif user_id == OWNER_ID:
             rank = "خاوەنی بۆت ⚡️👾"
        elif member.status == 'creator':
             rank = "خاوەنی  گرووپ 🫡⚡️"
        elif member.status == 'administrator':
             rank = "ئەدمینی گرووپ 🫡⚡️"
        else:
             rank = "ئەندام 🌚🫶🏻"
    except Exception as e:
        print(e)
        rank = "نازانم پلەت چییە 😒"
        await message.reply_text(
        text=f"""**سڵاو ئەزیزم : {italy} 💘\nمن بۆتی : {bot_name} 🫶🏻\nپلەت : {rank} 👻**""", reply_markup=keyboard)

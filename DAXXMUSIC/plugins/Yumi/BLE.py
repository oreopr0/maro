from pyrogram import Client, filters, idle
from DAXXMUSIC import app
from strings.filters import command
from pyrogram import filters
from pyrogram import Client



@app.on_message(filters.regex("^قول|^بلی") & filters.group)
async def say(app, message):
    if message.text.startswith("قول") and message.reply_to_message:
        txt = message.text.split(None, 1)[1]
        return await message.reply_to_message.reply(txt)

    elif message.text.startswith("بڵێ"):
        txt = message.text.split(None, 1)[1]
        return await message.reply(txt)



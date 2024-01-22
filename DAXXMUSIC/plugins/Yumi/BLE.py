from pyrogram import Client, filters, idle
from DAXXMUSIC import app
from strings.filters import command
from pyrogram import filters
from pyrogram import Client


@app.on_message(filters.regex("^بڵێ|^بلی") & filters.group)
async def say(app, message):
    if message.text.startswith("بلی") and message.reply_to_message:
        txt = message.text.split(None, 1)[1]
        return await message.reply_to_message.reply(txt)

    elif message.text.startswith("بڵێ"):
        txt = message.text.split(None, 1)[1]
        return await message.reply(txt)


@app.on_message(command(["دل","dl","dll","دڵ"]))
async def haert(c, msg):
    for i in range(45):
        await msg.edit(string_utils.shuffle("🩷❤️🧡💛💚🩵💙💜🖤🩶🤍🤎💔❤️‍🔥❤️‍🩹❣💕💞💓💗💖💘💝♥️‍"))
        time.sleep(0.1)


@app.on_message(command(["دلی","dlly","dli","دڵی"]))
async def haerts(c, msg):
    for i in range(1, 15):
        await msg.edit(string_utils.shuffle(
            "🩷❤️🧡💛💚🩵💙💜🖤🩶🤍🤎💔❤️‍🔥❤️‍🩹❣💕💞💓💗💖💘💝♥️🩷❤️🧡💛💚🩵💙💜🖤🩶🤍🤎💔❤️‍🔥❤️‍🩹❣💕💞💓💗💖💘💝♥️🩷❤️🧡💛💚🩵💙💜🖤🩶🤍🤎💔❤️‍🔥❤️‍🩹❣💕💞💓💗💖💘💝♥️‍"))
        time.sleep(0.1)

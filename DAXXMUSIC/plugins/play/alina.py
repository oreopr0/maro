import asyncio
from pyrogram import Client, filters
from strings.filters import command
from DAXXMUSIC.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from DAXXMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(command(["سلاو","slaw","سڵاو","سلام"]))
async def khalid(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""**بەخێربێی  {user} !\n\n• دوگمە دابگرە بۆ بینینی فەرمانەکانی ئەلینا**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝖠𝗅𝗂𝗇𝖺", callback_data=f"am"),
                ],
            ]
        ),
    )



@app.on_message(filters.regex("^چالاکی ئەلینا$") & filters.user(833360381))
async def ahtek(client: Client, message: Message):
    m_reply = await message.reply_text(f"**✧ اهلين مطوري ارحب\n- هذي احصائيات ميرا ياعيني :\n\n-› عدد المشتركين : 12478\n-› عدد المجموعات : 11346\n\n• تم زيادة 1204 مشترك ونقص 2103 مجموعة  في اخر 24 ساعة\n\n- عدد الطرد من بوتات اخرى : 843\n- طرد يدوي : 1302\n\n╼╾**")
    await m_reply_text("")


@app.on_message(filters.command("","."))
def vgdg(client,message):
        message.reply_text(
            f"""**✧ 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖡𝖺𝖻𝗒,
𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 -› [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅 ♪](t.me/IQ7amo)
𝖢𝗁𝖺𝗇𝗇𝖾𝗅 -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂](t.me/MGIMT)**""", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "نوێکارییەکانی ئەلینا 🍻", url=f"t.me/MGIMT")
                    ]
                ]
            ),
            disable_web_page_preview=True

        )




@app.on_message(command(["link delet","لینکی سرینەوە","لینکی سڕینەوە","بەستەری سڕینەوە","سووتاندنی ئەکاونت","سوتاندن","سووتاندن"]))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**• بەخێربێی ئەزیزم\n-› ئەمانە لینکی سووتاندنی سۆشیاڵ میدیان لەگەڵ بۆتێکی سووتاندنی تێلەگرام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖡𝗈𝗍 •", url=f"https://t.me/IQDLBOT"),
                ],[ 
                    InlineKeyboardButton(
                        "• 𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• 𝖲𝗇𝖺𝗉𝖢𝗁𝖺𝗍 •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• 𝖥𝖺𝖼𝖾𝖡𝗈𝗈𝗄 •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• 𝖳𝗐𝗂𝗍𝗍𝖾𝗋 •", url=f"https://mobile.twitter.com/settings/deactivate"),
                ],[
                    InlineKeyboardButton(
                        "نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT"),

                ],
            ]
        ),
    )




REPLY_MESSAGE = "**• بەخێربێی ئەزیزم کۆنتڕۆڵکردنی بە دوگمەکانی خوارەوەیە**"




REPLY_MESSAGE_BUTTONS = [

         [

             ("چۆن ئەلینا بەکاربێنم"),                   

             ("فەرمانی ئەلینا")

          ],
          [
              ("کەناڵ")
          ],
          [

             ("گەشەپێدەر"),

             ("سەرچاوە")

          ],

          [

             ("لادانی دووگمە")

          ]

]




  

@app.on_message(filters.regex("^ئەلینا$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("لادانی دووگمە"))
async def down(client, message):
          m = await message.reply("**• بە سەرکەوتوویی دووگمە لادرا\n• ئەگەر دەتەوێت جارێکی تر بیبینیتەوە بنووسە ئەلینا**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(command("چۆن ئەلینا بەکاربێنم"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**• بەخێربێی ئەزیزم بۆ چالاکردنی ئەلینا بە چەند هەنگاوێکە
1 • زیادی بکە و بیکە ئەدمین بە هەموو ڕۆڵەکان
2 • بۆ بینینی فەرمانەکان بنووسە [ فەرمانی ئەلینا یان ف ئەلینا ] بۆ پەخشکردن بنووسە [ پ ئەلینا یان پلەی + ناوی گۆرانی ]**
**• نموونە :** `پ ئەلینا کەمال محمد`
**• نموونە :** `پلەی کەمال محمد` 
**• بۆ هەبوونی هەر کێشە و ڕەخنەیەك پەیوەندی بکە بە گەشەپێدەر [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅 ♪](t.me/IQ7amo)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅", user_id=833360381),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت 🎻", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(command("سەرچاوە"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**• بەخێربێی ئەزیزم بۆ سەرچاوەی ئەلینا
• تایبەتمەندی بۆت : گۆرانی، پاراستن، داگرتن، وەڵامدانەوە
• بۆ هەبوونی هەر کێشە و ڕەخنەیەك پەیوەندی بکە بە گەشەپێدەر
𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 -› [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅 ♪](t.me/IQ7amo)
𝖢𝗁𝖺𝗇𝗇𝖾𝗅 -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂](t.me/MGIMT)
**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT"),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت 🎻", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



REPLY_MESSAGEE = "**• بەخێربێی ئەزیزم بۆ بەشی فەرمانەکانی ئەلینا**"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("فێرکاری پەخشکردن لە پلاتفۆڕمەکان")
          ],
          [
             ("فەرمانی گرووپ"),
             ("فەرمانی کەناڵ")
          ],
          [
             ("ڕێگای گەڕان"),
             ("ڕێگای گرێدانی کەناڵ")            
          ],
          [
             ("گەڕانەوە")
          ],
          [
            ("لادانی دووگمە")
          ]
]

  
@app.on_message(command("فەرمانی ئەلینا"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(command("گەڕانەوە"))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(command("فێرکاری پەخشکردن لە پلاتفۆڕمەکان"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""**✧ بەخێربێن بۆ بەشی پەخشکردنی پلاتفۆڕمەکان\n- پشتگیری لە پلاتفۆڕمەکان ↓\n\n• 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆\n• 𝖸𝗈𝗎𝖳𝗎𝖻𝖾\n• 𝖲𝗈𝗎𝗇𝖽𝖢𝗅𝗈𝗎𝖽\n• 𝖠𝗉𝗉𝗅𝖾𝖬𝗎𝗌𝗂𝖼\n• 𝖲𝗉𝗈𝗍𝗂𝖿𝗒\n\n• [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅](t.me/IQ7amo) لە هەبوونی هەر کێشەیەك پەیوەندی بە خاوۆنی بۆت بکە\n• [𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂](t.me/MGIMT)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت 🎻", url=f"https://t.me/IQMCBOT?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(command("فەرمانی گرووپ"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n**╭── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╮**\n\n **✧ فەرمانی پەخشکردن لە گرووپ**\n\n**• پلەی + ناوی گۆرانی یان ڕیپلەی لینك** \n-› بۆ پەخشکردنی گۆرانی لە گرووپ\n\n• **وەستان** یان **ڕاگرتن**\n-› بۆ وەستاندنی پەخشکردن\n\n• **سکیپ** یان **دواتر**\n-› بۆ گۆڕینی گۆرانی دواتر\n\n• **وەستانی کاتی** یان **وسبە**\n-› بۆ وەستاندنی پەخشکردن بۆ ماوەیەکی کاتی\n\n• **د** یان **دەستپێکردنەوە**\n-› بۆ دەستپێکردنەوەی پەخشکردن کاتێ وەستاوە\n\n**╰── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/EHS4SS"),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(command("فەرمانی کەناڵ"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n**╭── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╮**\n\n** ✧ فەرمانی پەخشکردن لە کەناڵ**\n\n**• پ کەناڵ + ناوی گۆرانی یان ڕیپلەی لینك** \n-› بۆ پەخشکردنی گۆرانی لە کەناڵ\n\n**• وەستان**\n-› بۆ وەستانی هەموو گۆرانیەکان کۆتایی هاتن\n\n**• دواتر**\n-› بۆ گۆڕینی گۆرانی بۆ گۆرانی دواتر\n\n**• وەستانی کاتی**\n-› بۆ وەستانی پەخشکردن بۆ ماوەیەکی کاتی\n\n**• دەستپێکردنەوە**\n-› بۆ دەستپێکردنەوەی پەخشکردن کاتێ وەستاوە\n\n**╰── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/EHS4SS"),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت 🎻", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(command("ڕێگای گەڕان"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""**بەخێربێن بۆ بەشی داگرتن ♪\nبۆ گەڕانی گۆرانی یان ڤیدیۆ و داگرتنی ↓\n\n[ گەڕان + ناوی گۆرانی ..]\n\nنموونە -› گەڕان قادر کابان فریشتە**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/EHS4SS"),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت 🎻", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(command("ڕێگای گرێدانی کەناڵ"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا**\n**◌پەخشکردن لە کەناڵ چەند هەنگاوێکی پێویستە◌ :**\n\n1 -› بۆت زیادبکە کەناڵ و بیکە بە ئەدمین\n2 -› بگەڕێوە گرووپ و بنووسە { **گرێدان + یوزەری کەناڵ** }\n3 -› **دەست بدە لە فەرمانی پەخشکردن بۆ زانینی پەخشکردن**\n\n**✶ پەیوەندی کردن - @IQ7amo**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/EHS4SS"),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت 🎻", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

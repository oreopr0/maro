import asyncio
from pyrogram import Client, filters
from strings import get_command
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

@app.on_message(filters.regex("^$"))
async def khalid(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""**بەخێربێی {user} !\n- دوگمە دابگرە بۆ بینینی فەرمانەکانی ئەلینا**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "فەرمانەکان", callback_data=f"am"),
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
            f"""✧ Welcome Baby,
𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 -› [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅 ♪](t.me/IQ7amo)
𝖢𝗁𝖺𝗇𝗇𝖾𝗅 -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂](t.me/MGIMT)""", 
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

                ],
            ]
        ),
    )


@app.on_message(filters.command("ميرا نادي المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001801583479, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- **ابشر ياعيوني ارسلت للمطور بيخش القروب ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت عشات تشوف التحديثات** -› [• Source Mira •](t.me/NvvvC)""", disable_web_page_preview=True     
    )


REPLY_MESSAGE = "**• بەخێربێی ئەزیزم کۆنتڕۆڵکردنی بە دوگمەکانی خوارەوەیە"




REPLY_MESSAGE_BUTTONS = [

         [

             ("چۆن ئەلینا بەکاربێنم"),                   

             ("فەرمانی ئەلینا")




          ],

          [

             ("المطور"),

             ("السورس")

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

@app.on_message(filters.regex("لادانی دووگمە") & filters.group)
async def down(client, message):
          m = await message.reply("**- ابشر تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب ميرا**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command("چۆن ئەلینا بەکاربێنم"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **هلا والله ياعيني عشان تفعل بوت ميرا اتبع الخطوات الي بالاسفل**
1 • ارفعه مشرف بكل الصلاحيات 
2 • لو تبي تشوف الاوامر اكتب [ م الاوامر ] ولو تبي تشغل على طول اكتب ميرا شغلي + اسم المقطع الصوتي
• مثال : ميرا شغلي واتنسيت
- لو واجهت مشكله كلم مطور البوت ~ @PsPsP""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "Khaled", user_id=2089102006),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & command("السورس"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين فيك بسورس ميرا ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت**
مطور السورس -› [Khaled](t.me/PsPsP)
قناة السورس -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂](t.me/NvvvC)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT"),
                ],[
                    InlineKeyboardButton(
                        "• زیادم بکە بۆ گرووپت", url=f"https://t.me/IQMCBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



REPLY_MESSAGEE = "- هلا فيك في قسم اوامر ميرا"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("فێرکاری پەخشکردن لە پلاتفۆڕمەکان")
          ],
          [
             ("فەرمانی گرووپ"),
             ("فەرمانی کەناڵ")
          ],
          [
             ("ڕێگای گەڕان")
             ("ڕێگای گرێدانی کەناڵ")            
          ],
          [
             ("")
          ],
          [
            ("لادانی دووگمە")
          ]
]

  
@app.on_message(filters.group & command("فەرمانی ئەلینا"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.group & command(""))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.group & command("فێرکاری پەخشکردن لە پلاتفۆڕمەکان"))
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

@app.on_message(filters.group & command("فەرمانی گرووپ"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n**╭── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╮**\n\n **✧ فەرمانی پەخشکردن لە گرووپ**\n\n**• پلەی + ناوی گۆرانی یان ڕیپلەی لینك** \n-› بۆ پەخشکردنی گۆرانی لە گرووپ\n\n• **وەستان** یان **ڕاگرتن**\n-› بۆ وەستاندنی پەخشکردن\n\n• **سکیپ** یان **دواتر**\n-› بۆ گۆڕینی گۆرانی دواتر\n\n• **وەستانی کاتی** یان **وسبە**\n -› بۆ وەستاندنی پەخشکردن بۆ ماوەیەکی کاتی\n\n• **د** یان **دەستپێکردنەوە**\n -› بۆ دەستپێکردنەوەی پەخشکردن کاتێ وەستاوە\n\n**╰── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╯**""",
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


@app.on_message(filters.group & command("فەرمانی کەناڵ"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n**╭── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╮**\n\n** ✧ فەرمانی پەخشکردن لە کەناڵ**\n\n**• پ کەناڵ + ناوی گۆرانی یان ڕیپلەی لینك** \n-› بۆ پەخشکردنی گۆرانی لە کەناڵ\n\n**• وەستان**\n-› بۆ وەستانی هەموو گۆرانیەکان کۆتایی هاتن\n\n**• دواتر**\n-› بۆ گۆڕینی گۆرانی بۆ گۆرانی دواتر\n\n**• وەستانی کاتی**\n -› بۆ وەستانی پەخشکردن بۆ ماوەیەکی کاتی\n\n**• دەستپێکردنەوە**\n -› بۆ دەستپێکردنەوەی پەخشکردن کاتێ وەستاوە\n\n**╰── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╯**""",
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



@app.on_message(filters.group & command("ڕێگای گەڕان"))
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


@app.on_message(filters.group & command("ڕێگای گرێدانی کەناڵ"))
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

import asyncio


import random
from DAXXMUSIC import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
from config import OWNER_ID

dev = (OWNER_ID)


txt = [
            "**اضحك يعم محدش واخد منها حاجه ♥♥"


             "😂😂😂😂😂😂😂",
            

    
            
            
            "** لول😂😂**",
            
            
 
            
            

        ]
txt1 = [

            "**مفيش حاجه بتدحك ع فكرا♥️😻**",


             "**يا ضحك😂😂**",
            

            "**ضحكني معاك 😂😂**",
            
            
          
            
 
            
            

        ]

        
        


@app.on_message(command(["ههه","😂😂","😂😂😂","😂🤣","ههههههههههههههههههه","😂😂😂😂😂😂"]))


async def cutt(client: Client, message: Message):

     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(

         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       

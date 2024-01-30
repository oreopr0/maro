from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from DAXXMUSIC import app
from pyrogram.types import Message
# -----------------




# --------------------------------------------------------------------------
mongo_uri = "mongodb+srv://mgimt:VmWx4PiUcqDNzsko@cluster0.tqkwsba.mongodb.net/?retryWrites=true&w=majority"
database_name = "MONGODB"
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------

mongo_client = MongoClient(mongo_uri)
db = mongo_client[database_name]
top_members_collection = db["rank_db"]

user_data = {}

# ----------------



@app.on_message(filters.command(["top10","rank"]))
def top_members(_, message):
    top_members = top_members_collection.find().sort("total_messages", -1).limit(10)
    
    response = "**📈 لیستی چالاکی\n**"
    for idx, member in enumerate(top_members, start=1):
        user_id = member["_id"]
        
        try:
            user = app.get_users(user_id)
            Mention = user.mention if user.mention else "none"
        except PeerIdInvalid:
            first_name = "نەناسراو"
        
        total_messages = member["total_messages"]
        user_info = f"**{idx} 👤{Mention}, •{total_messages}\n**"
        response += user_info

    message.reply_text(response)


@app.on_message()
def handle_messages(_, message):
    user_id = message.from_user.id
    
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1
    
    top_members_collection.update_one({"_id": user_id}, {"$inc": {"total_messages": 1}}, upsert=True)

# ------------------------------


# --------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------

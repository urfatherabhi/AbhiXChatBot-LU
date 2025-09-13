

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from AbhiXChat import AbhiXChat
from AbhiXChat.database.chats import add_served_chat
from AbhiXChat.database.users import add_served_user
from AbhiXChat.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://graph.org/file/1e0af186d0575a7d6a650.jpg",
    "https://graph.org/file/83312f735f032270a4c23.jpg",
    "https://graph.org/file/dc111a1c1358c553ea604.jpg",
    "https://graph.org/file/d8db306e9e0b0504718b3.jpg",
    "https://graph.org/file/804fa956a84862b547fc5.jpg",
    "https://graph.org/file/0f89cd8d55fd9bb5130e1.jpg",
    "https://graph.org/file/e5eb7673737ada9679b47.jpg",
    "https://graph.org/file/2e4dfe1fa5185c7ff1bfd.jpg",
    "https://graph.org/file/36af423228372b8899f20.jpg",
    "https://graph.org/file/c698fa9b221772c2a4f3a.jpg",
    "https://graph.org/file/61b08f41855afd9bed0ab.jpg",
    "https://graph.org/file/744b1a83aac76cb3779eb.jpg",
    "https://graph.org/file/814cd9a25dd78480d0ce1.jpg",
    "https://graph.org/file/e8b472bcfa6680f6c6a5d.jpg",
]


#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@AbhiXChat.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{AbhiXChat.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [᚛᚜‹‹Cʀᴀᴢʏ々ܔHᴜɴᴛᴇʀ››᚛᚜❣️](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)

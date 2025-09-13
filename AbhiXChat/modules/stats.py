from pyrogram import filters, Client
from pyrogram.types import Message

from AbhiXChat import OWNER, AbhiXChat
from AbhiXChat.database.chats import get_served_chats
from AbhiXChat.database.users import get_served_users


@AbhiXChat.on_cmd("stats")
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )

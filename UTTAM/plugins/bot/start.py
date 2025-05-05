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
    """**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ─────•\n┆⚘ ʜᴇʏ, ɪ ᴀᴍ : [˹ 🅤sᴇʀʙᴏᴛ ˼](t.me/USERBOT_ROBOT)\n┆⚘ ᴍᴏʀᴇ ᴀɴɪᴍᴀᴛɪᴏɴ,ғᴜɴ\n┊⚘ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟ ᴜsᴇʀʙᴏᴛ\n╰─────────────────────•\n❍ ʜσᴡ ᴛσ υsє ᴛʜɪs ʙσᴛ - [ᴛɪᴘs ʜᴇʀᴇ](https://t.me/RADHE_ALLBOT) \n❍ sᴛꝛɪηɢ sєᴄᴛɪση ʙσᴛ ⁚ [sᴇssɪᴏɴ-ʙᴏᴛ](https://t.me/STRING_SESSION_GENN_BOT) \n•──────────────────────•\n❍ ᴄʟσηє ⁚ /clone [ sᴛʀɪɴɢ sᴇssɪᴏɴ ]\n•──────────────────────•\n❍ ᴘσɯҽɾҽᴅ ʙу ⏤‌‌‌‌  [𝙱𝙾ᴛᴍɪɴᴇ-ᴛᴇᴄʜ](https://t.me/BOTMINE_TECH) \n•──────────────────────•**"""
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/TEAM_INDIANS_BOT"),
                InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇ ˼", url="https://t.me/BOTMINE_TECH"),
            ],
            [
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/BOTMINE_SUPPORT"),
                InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", url="https://t.me/sanataniiMusicBot"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("ᴜsᴀɢᴇ:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("🎨 ᴘʀᴏᴄᴇssɪɴɢ.....✲")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="UTTAM/plugins"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" Successfully host 🎨 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

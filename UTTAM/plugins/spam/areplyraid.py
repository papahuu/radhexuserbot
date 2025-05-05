import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from UTTAM.database.rraid import get_rraid_users, rraid_user
from UTTAM import SUDO_USER
from .replyraid import RAIDS
from UTTAM.plugins.basic.profile import extract_user

# Make sure SUDO_USER is a list of ints
SUDO_USERS = SUDO_USER if isinstance(SUDO_USER, list) else [SUDO_USER]

@Client.on_message(filters.command(["replyraid"], ".") & (filters.me | filters.user(SUDO_USERS)))
async def activate_replyraid(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")

    try:
        if args:
            user = await client.get_users(args)
        elif reply:
            user = reply.from_user
        else:
            return await ex.edit("`Please specify a valid user!`")

        if user.id == client.me.id:
            return await ex.edit("**Okay Sure.. 🐽**")
        if user.id in SUDO_USERS:
            return await ex.edit("**Failed! This user is a sudo user.. 🐽**")

        if user.id in (await get_rraid_users()):
            return await ex.edit("Replyraid is already activated on this user")

        await rraid_user(user.id)
        RAIDS.append(user.id)

        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) is now under ReplyRaid!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")

# This listener actually performs the raid
@Client.on_message(filters.group & filters.text)
async def replyraid_action(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else None
    if not user_id:
        return

    # Check if user is in active replyraid list
    if user_id in RAIDS or user_id in (await get_rraid_users()):
        try:
            await asyncio.sleep(1)  # Optional delay
            reply = await message.reply(
                choice([
                    "Chup baith ja!",
                    "Teri bakwaas sunne ka time nahi.",
                    "Phirse bola to gaali padegi!",
                    "Aukat me reh.",
                    "Ek number ka chomu hai tu!"
                ])
            )
            await asyncio.sleep(10)
            await reply.delete()
        except Exception as e:
            print(f"[ReplyRaid Error] {e}")

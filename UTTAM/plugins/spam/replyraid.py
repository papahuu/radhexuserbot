from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Add your sudo users here
DEVS = 7403621976
# Superfast unlimited .raid command
@Client.on_message(filters.command("raid", ".") & (filters.me | filters.user(SUDO_USERS)))
async def raid(client: Client, message: Message):
    try:
        count = int(message.command[1])
    except (IndexError, ValueError):
        return await message.reply("Usage: .raid <count>")

    text = "RAID IN PROGRESS!"

    for _ in range(count):
        await message.reply(text)
        await asyncio.sleep(0.1)

# Superfast unlimited .dmraid command
@Client.on_message(filters.command("dmraid", ".") & (filters.me | filters.user(SUDO_USERS)))
async def dmraid(client: Client, message: Message):
    try:
        count = int(message.command[1])
    except (IndexError, ValueError):
        return await message.reply("Usage: .dmraid <count> (reply to user or provide ID)")

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        try:
            user_id = int(message.command[2])
        except (IndexError, ValueError):
            return await message.reply("Reply to a user or give user ID.")

    text = "This is a DM raid message!"

    for _ in range(count):
        try:
            await client.send_message(user_id, text)
            await asyncio.sleep(0.2)
        except Exception as e:
            return await message.reply(f"Error: {e}")

    await message.reply(f"Sent {count} messages to {user_id}.")

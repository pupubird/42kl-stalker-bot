import os
import discord
from dotenv import load_dotenv
from src.location import Location

load_dotenv()
client = discord.Client()

try:
    l = Location()
except Exception:
    print("Invalid 42 API Key.")


async def get_location(message, username):
    await message.channel.send("Finding {}!".format(username))
    l.refresh_locations()

    try:
        location = l.search(username)
    except Exception:
        await message.channel.send("42 API Key expired!")
        return
    if not location:
        await message.channel.send(
            "{} is not in the building!\nPlease check if you entered the correct username!".format(
                username
            )
        )
        return
    await message.channel.send(location)


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/find"):
        msg = message.content

        args = msg.split()
        if len(args) < 2:
            await message.channel.send("Please enter a username!")
        elif len(args) == 2:
            await get_location(message, args[1])
        else:
            await message.channel.send("Please only enter one username!")


client.run(os.getenv("TOKEN"))

import os
import discord
from dotenv import load_dotenv
from src.location import Location

load_dotenv()
client = discord.Client()

async def get_location(message, username):
  await message.channel.send('Finding {}!'.format(username))

  l = Location()

  # Optional
  l.refresh_locations()
  location = l.search(username)

  if not location:
    await message.channel.send('{} is not in the building!\nPlease check if you entered the correct username!'.format(username))
    return
  await message.channel.send(location)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('/find'):
    msg = message.content

    args = msg.split()
    if len(args) < 2:
      await message.channel.send('Please enter a username!')
    elif len(args) == 2:
      await get_location(message, args[1])
    else:
      await message.channel.send('Please only enter one username!')

client.run(os.getenv('TOKEN'))
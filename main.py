import logging
import discord
import os
import sys
from arguments_from_string import handle_atom_call

TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    sys.exit('DISCORD_TOKEN not set')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# create logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
console_hander = logging.StreamHandler()
console_hander.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s",
                              "%Y-%m-%d %H:%M:%S")
# add formatter to ch
console_hander.setFormatter(formatter)

# add ch to logger
logger.addHandler(console_hander)


@client.event
async def on_ready():
    logger.info("AtomInstructor connected to Discord")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not isinstance(message.channel, discord.channel.DMChannel):
        return

    response = handle_atom_call(message.content, logger)

    if response:
        await message.channel.send(response)


client.run(TOKEN)

import logging

import discord
import os
from atom_instructions import get_atom_instruction_string
from arguments_from_string import get_arguments_from_string, create_parser, get_parser_help_string, handle_atom_call

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# create logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s",
                              "%Y-%m-%d %H:%M:%S")
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


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

import logging

import discord
import os
import sys
from io import StringIO
from atom_instructions import get_atom_instruction_string
from arguments_from_string import get_arguments_from_string, create_parser

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

    content: str = message.content
    if content.startswith('!atomhelp') or content.startswith('!atom help'):
        logger.info("!atomhelp called")
        parser = create_parser()

        # redirect print to mystdout
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        # perform printing action
        parser.print_help()
        # restore original cout
        sys.stdout = old_stdout

        response = mystdout.getvalue()
        await message.channel.send(response)

    elif content.startswith('!atom') or content.startswith('!Atom') or content.startswith('!ATOM'):
        logger.info("!atom called")
        try:
            args = get_arguments_from_string(content)
            response = get_atom_instruction_string(args)
            await message.channel.send(response)
        except:
            logger.error("!atom failed: '" + content + "'")
            await message.channel.send(":exclamation: AtomInstructor collapses")


client.run(TOKEN)

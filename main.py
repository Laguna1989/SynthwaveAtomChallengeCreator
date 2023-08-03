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


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not isinstance(message.channel, discord.channel.DMChannel):
        return

    content: str = message.content
    if content.startswith('!atomhelp'):
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
        try:
            args = get_arguments_from_string(content)
            response = get_atom_instruction_string(args)
            await message.channel.send(response)
        except:

            await message.channel.send(":exclamation: AtomInstructor collapses")


client.run(TOKEN)

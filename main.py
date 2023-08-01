import discord
import os

from atom_arguments import AtomArguments
from atom_instructions import get_atom_instruction_string
from arguments_from_string import get_arguments_from_string

# print(create_atom_instruction_string())

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
    content: str = message.content
    if content.startswith('!atom') or content.startswith('!Atom') or content.startswith('!ATOM'):
        args = get_arguments_from_string(content)

        response = get_atom_instruction_string(args)
        await message.channel.send(response)


client.run(TOKEN)

import discord
import os

from atom_instructions import get_atom_instruction_string

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

    if message.content == '!atom' or message.content == '!Atom' or message.content == '!ATOM':
        response = get_atom_instruction_string()
        await message.channel.send(response)

client.run(TOKEN)
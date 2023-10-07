import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='~')
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
         return
    if message.content.startswith('$hello'):
         await message.channel.send('Hello!')
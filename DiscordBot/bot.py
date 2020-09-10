import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NzUzMzU4NDU1OTM4NzQ0MzIz.X1lBvA.QyyNneYEDH5jyWc5NFN6SHvEYAQ')
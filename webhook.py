import aiohttp
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=',')


@bot.command()
async def webhook(ctx, username, *, message):
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url('URL_HERE', session=session)
        await webhook.send(message, username=username)
        
# Usage:
#   ,webhook [WEBHOOK USERNAME HERE] [TEXT HERE]
#   you can use ,webhook "John Doe" Lorem Ipsum Dolor Sit Amet
#   for a name with more words
#   simple example:
#   ,webhook John Lorem Ipsum Dolor Sit Amet
#            ^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^        
#           [Name][Text as long as you want]     
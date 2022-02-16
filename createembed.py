import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=',')

@bot.command()
async def ce(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await bot.wait_for('message', check=check)
  
    await ctx.send('Waiting for a description')
    desc = await bot.wait_for('message', check=check)
    x = ctx.message.author

    embed = discord.Embed(title=title.content, description=desc.content, color=0x72d345)
    embed.set_author(name=x.display_name, icon_url=x.display_avatar)
    await ctx.send(embed=embed)
    
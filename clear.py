from discord.ext import commands


bot = commands.Bot(command_prefix=',')


@bot.command()
async def clear(ctx, number:int = 5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=number)
    await ctx.send(f'Cleared {number} messages', delete_after=1)

# Usage: ,clear [NUMBER OF MESSAGES]
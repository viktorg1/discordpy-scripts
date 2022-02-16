from discord.ext import commands


bot = commands.Bot(command_prefix=',')


@bot.command()
async def react(ctx, id, emoji):
    message = await ctx.fetch_message(id)
    await message.add_reaction(emoji)
    
# Usage: ,react [MESSAGE_ID] [EMOJI]
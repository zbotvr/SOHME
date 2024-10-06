import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx, member: discord.Member, amount: int):
    for i in range(amount):
        await ctx.send(f"{member.mention} ping {i+1}!")

bot.run('MTI4ODY0NDc5MjgyNTE1MTQ4OA.GIo-Lr.MHZ64GvbokEcya5eqXiKDdDJpL4UzTYUaJwJvU')

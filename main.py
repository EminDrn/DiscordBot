import discord
from discord.ext import commands
from utils import *
from  functions import *
itents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='!mm ', itents=itents)
game = Game()

@Bot.event
async def on_ready():
    print("ben hazırım!")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name ="genel")
    await channel.send(f"{member} aramiza katıldı.Hoş geldin")
    print(f"{member} aramiza katıldı.Hoş geldin")


@Bot.command()
async def hosgeldin(ctx , *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('Hoş buldum :)')

@Bot.command(aliases = ["game", "oyun"])
async def selam(ctx , *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('as!')
@commands.has_role("💫Kurucu💫")
@Bot.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

@commands.has_role("💫Kurucu💫")
@Bot.command(aliases = ["copy"])
async def clone_channel(ctx):
    await ctx.channel.clone()
@commands.has_role("💫Kurucu💫")
@Bot.command()
async def kick(ctx, member = discord.Member, *args , reason = "Yok"):
    member.kick(reason = reason)
@commands.has_role("💫Kurucu💫")
@Bot.command()
async def ban(ctx, member = discord.Member, *args , reason = "Yok"):
    member.kick(reason = reason)

Bot.run(TOKEN)

import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix=".", intents=intents)

@client.command()
async def hello(ctx, age, *, name):
    await ctx.send(f"hello {ctx.author.mention} you're named {name} and are {age} years old")


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

client.run("YOUR TOKEN HERE")

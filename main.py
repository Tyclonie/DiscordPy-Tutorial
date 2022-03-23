import os
import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix=".", intents=intents)

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, *, cog_name):
    try:
        client.unload_extension(f"cogs.{cog_name}")
        await ctx.send("Unloaded")
    except Exception as e:
        await ctx.send(f"Failed: {str(e)}")

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, *, cog_name):
    try:
        client.reload_extension(f"cogs.{cog_name}")
        await ctx.send("Reloaded")
    except Exception as e:
        await ctx.send(f"Failed: {str(e)}")

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, *, cog_name):
    try:
        client.load_extension(f"cogs.{cog_name}")
        await ctx.send("Loaded")
    except Exception as e:
        await ctx.send(f"Failed: {str(e)}")

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{file[:-3]}")
                print(f"Loaded {file[:-3]}")
            except Exception as e:
                print(f"Failed to load {file[:-3]} because: {str(e)}")

client.run("YOUR TOKEN HERE")

import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

client.run("OTU1OTI2ODA1NTk5MTA5MTIx.YjoyNg.wbO4VtF_Uwa3Gz1G8jyN7xJ6RL0")

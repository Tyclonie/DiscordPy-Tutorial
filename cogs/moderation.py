import discord
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed()
        try:
            await member.kick(reason=reason)
            embed.add_field(name="Kick log", value=f"{ctx.author.mention} has kicked {member.mention} for {reason}")
        except discord.errors.Forbidden:
            embed.add_field(name="Kick log", value=f"I cannot kick this user")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed()
        try:
            await member.ban(reason=reason)
            embed.add_field(name="Ban log", value=f"{ctx.author.mention} has banned {member.mention} for {reason}")
        except discord.errors.Forbidden:
            embed.add_field(name="Ban log", value=f"I cannot ban this user")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        embed = discord.Embed()
        try:
            await ctx.channel.purge(limit=amount+1)
            embed.add_field(name="Purge log", value=f"{ctx.author.mention} has eaten {str(amount)} of message(s) in {ctx.channel.mention}")
        except discord.errors.Forbidden:
            embed.add_field(name="Purge log", value=f"I cannot purge here")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Utility(client))

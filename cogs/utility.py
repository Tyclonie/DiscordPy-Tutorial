from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, number_one: int, number_two: int):
        await ctx.send(str(number_one + number_two))

    @commands.command()
    async def sub(self, ctx, number_one: int, number_two: int):
        await ctx.send(str(number_one - number_two))

    @commands.command()
    async def mul(self, ctx, number_one: int, number_two: int):
        await ctx.send(str(number_one * number_two))

    @commands.command()
    async def div(self, ctx, number_one: int, number_two: int):
        await ctx.send(str(number_one / number_two))


def setup(client):
    client.add_cog(Utility(client))

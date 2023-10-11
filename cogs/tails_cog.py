import random
from nextcord.ext import commands


class orzel_czy_reszka(commands.Cog, object):
    @commands.command()
    async def moneta(self, ctx, num=2):
        res = random.randint(1, num)

        if res == 1:
            await ctx.send(f':coin:')
        elif res == 2:
            await ctx.send(f':eagle:')


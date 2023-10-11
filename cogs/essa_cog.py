import random
from nextcord.ext import commands
from config import config


class Inne(commands.Cog, object):
    @commands.command()
    async def essa(self, ctx, num=100):
        res = random.randint(1, num)

        if res <= 25:
            await ctx.send(f'Twoja essa wynosi {res}  :sleeping: ')
        elif res <= 50:
            await ctx.send(f'Twoja essa wynosi {res}  :rolling_eyes:')
        elif res <= 75:
            await ctx.send(f'Twoja essa wynosi {res}  :thumbsup: ')
        elif res <= 90:
            await ctx.send(f'Twoja essa wynosi {res}  :scream_cat: ')
        elif res <= 100:
            await ctx.send(f'Twoja essa wynosi {res}  :fire::fire::fire: ')

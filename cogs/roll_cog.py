import nextcord
from nextcord.ext import commands
import random
from config import config

class losowanie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=config.HELP_ROLL_LONG, help=config.HELP_ROLL_SHORT)
    async def roll(self, ctx, *names):
        names = list(names)
        random.shuffle(names)

        if not names:
            await ctx.send("Brak imion do losowania!")
            return

        result = "\n".join(names)
        await ctx.send(f"Losowanie:\n{result}")
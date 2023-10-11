from PIL import Image
from io import BytesIO
import nextcord
from nextcord.ext import commands
from config import config


class profilepic(commands.Cog):
    @commands.command(description=config.HELP_PROFILEPIC_LONG, help=config.HELP_PROFILEPIC_SHORT)
    async def profilepic(self,ctx, user: nextcord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("images/wanted.jpg")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((400, 400))
        wanted.paste(pfp)
        wanted.save("images/profile.jpg")

        await ctx.send(file=nextcord.File("images/profile.jpg"))

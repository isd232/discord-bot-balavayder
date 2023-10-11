import os
import nextcord
from nextcord.ext import commands
from config import config


from cogs.reddit_cog import Subreddity
from cogs.essa_cog import Inne
from cogs.profilepic_cog import profilepic
# from cogs.openai import MyClient
from cogs.tails_cog import orzel_czy_reszka
from cogs.roll_cog import losowanie

from musicbot.audiocontroller import AudioController
from musicbot.settings import Settings
from musicbot.utils import guild_to_audiocontroller, guild_to_settings


intents = nextcord.Intents.all()


initial_extensions = ['musicbot.commands.music',
                      'musicbot.commands.general', 'musicbot.plugins.button']


bot = commands.Bot(command_prefix='!',
                   case_insensitive=True, intents=intents)

# bot.add_cog(MyClient())
bot.add_cog(Subreddity())
bot.add_cog(Inne())
bot.add_cog(profilepic())
bot.add_cog(orzel_czy_reszka())
bot.add_cog(losowanie(bot))

if __name__ == '__main__':

    config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

    if config.BOT_TOKEN == "":
        print("Error: No bot token!")
        exit()

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)


@bot.event
async def on_ready():
    print(config.STARTUP_MESSAGE)
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game(name="gowno gowno {}help".format(config.BOT_PREFIX)))

    for guild in bot.guilds:
        await register(guild)
        print("Joined {}".format(guild.name))

    print(config.STARTUP_COMPLETE_MESSAGE)


@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)


async def register(guild):

    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)

    sett = guild_to_settings[guild]

    try:
        await guild.me.edit(nick=sett.get('default_nickname'))
    except:
        pass

    if config.GLOBAL_DISABLE_AUTOJOIN_VC == True:
        return

    vc_channels = guild.voice_channels

    if sett.get('vc_timeout') == False:
        if sett.get('start_voice_channel') == None:
            try:
                await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
            except Exception as e:
                print(e)

        else:
            for vc in vc_channels:
                if vc.id == sett.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                    except Exception as e:
                        print(e)

bot.run(config.BOT_TOKEN, reconnect=True)
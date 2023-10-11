import nextcord
from nextcord.ext import commands
import random
from asyncpraw import Reddit
from config import config
from config.config import client_id, user_agent, password, username, client_secret, HELP_REDDIT_SHORT

reddit = Reddit(client_id=client_id,
               client_secret=client_secret,
               username=username,
               password=password,
               user_agent=user_agent)


class SubredditHelper:
    def __init__(self, subreddit_name):
        self.subreddit_name = subreddit_name

    async def get_random_submission(self):
        subreddit = await reddit.subreddit(self.subreddit_name)
        all_subs = []

        async for submission in subreddit.hot(limit=100):
            if not submission.is_self:  # Sprawdź, czy post zawiera link do obrazu/wideo
                all_subs.append(submission)

        if not all_subs:
            return None, None  # Jeśli nie ma obrazu/wideo, zwróć None

        random_sub = random.choice(all_subs)

        name = random_sub.title[:256]
        url = random_sub.url

        print(f"The URL is: {url}")  # Debugging line

        return name, url


class Subreddity(commands.Cog):
    @commands.command(description=config.HELP_REDDIT_LONG, help=config.HELP_REDDIT_SHORT)
    async def reddit(self, ctx, subreddit_name):
        helper = SubredditHelper(subreddit_name)
        name, url = await helper.get_random_submission()

        if name is None or url is None:
            await ctx.send("Nie znaleziono obrazu lub wideo.")
            return

        em = nextcord.Embed(title=name)
        em.set_image(url=url)

        await ctx.send(embed=em)

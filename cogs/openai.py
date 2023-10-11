# import os
# import nextcord
# import openai
# from config import config
# from nextcord.ext import commands
# from OPENAI.response import chatgpt_response
#
# openai.api_key = config.CHATGPT_API_KEY
#
# class MyClient(commands.Cog):
#
#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.author.bot or message.guild is None:
#             return
#
#         command = None
#
#         for text in ['!ai', '!bot', '!chatgpt']:
#             if message.content.startswith(text):
#                 command = text
#                 user_message = message.content.replace(text, '').strip()
#
#         if command in ['!ai', '!bot', '!chatgpt']:
#             bot_response = chatgpt_response(prompt=user_message)
#             await message.channel.send(f"Answer: {bot_response}")
#
#     @commands.command(name='ai')
#     async def ai(self, ctx, *, user_message):
#         if ctx.author.bot:
#             return
#
#         command = None
#
#         for text in ['!ai', '!bot', '!chatgpt']:
#             if user_message.startswith(text):
#                 command = text
#                 user_message = user_message.replace(text, '').strip()
#
#         if command in ['!ai', '!bot', '!chatgpt']:
#             bot_response = chatgpt_response(prompt=user_message)
#             await ctx.send(f"Answer: {bot_response}")

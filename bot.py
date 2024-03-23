import os
import base64
import openai
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is connected and ready!')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    text_content = message.content
    print(text_content)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text_content}]
    )

    await message.channel.send(response.choices[0].message.content)

bot.run(discord_token)


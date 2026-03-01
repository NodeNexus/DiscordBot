import os
import discord
from discord.ext import commands
import asyncio
from flask import Flask
from threading import Thread

TOKEN = os.getenv("TOKEN")
GUILD_ID = 1401261289434775562
VOICE_CHANNEL_ID = 1442561521778425886

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def ensure_voice():
    await bot.wait_until_ready()
    guild = bot.get_guild(GUILD_ID)

    while not bot.is_closed():
        try:
            vc = guild.get_channel(VOICE_CHANNEL_ID)
            if not guild.voice_client:
                await vc.connect()
                print("Joined VC permanently.")
        except Exception as e:
            print("Voice error:", e)

        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.loop.create_task(ensure_voice())

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=10000)

Thread(target=run_web).start()

bot.run(TOKEN)

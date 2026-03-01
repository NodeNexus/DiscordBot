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
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ---------- Voice Join Logic ----------
async def join_voice():
    await bot.wait_until_ready()
    await asyncio.sleep(5)

    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print("Guild not found")
        return

    channel = guild.get_channel(VOICE_CHANNEL_ID)
    if not channel:
        print("Voice channel not found")
        return

    if not guild.voice_client:
        try:
            await channel.connect(reconnect=True)
            print("Joined voice channel")
        except Exception as e:
            print("Voice connect error:", e)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.loop.create_task(join_voice())

@bot.event
async def on_disconnect():
    print("Bot disconnected")

# ---------- Web Server for Render ----------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=10000)

Thread(target=run_web).start()

bot.run(TOKEN)

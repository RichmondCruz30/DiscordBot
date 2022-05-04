#bot.py
from dis import dis, disco

from unittest import getTestCaseNames
import discord
import youtube_dl
from gtts import gTTS
import os
import time
from random import randrange

from discord.ext import commands,tasks
from dotenv import load_dotenv
from discord.utils import get
from discord import TextChannel
from discord import FFmpegPCMAudio

#needed to hide information

load_dotenv()
TOKEN = 'OTMzMTc3OTg4MTUxOTIyNjg4.YedvuQ.LHJf4yYV7ejEua8WogcEjarPWFs'
GUILD = 'BANGABLE'

client = discord.Client()

bot = commands.Bot(command_prefix='**')

#outdated

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if 'tangina mo ivan' in message.content.lower():        
        await message.channel.send('Tangina mo Ivan!!<@801171319437000724>')

@client.event
async def on_message(message):
    if 'tangina mo charles' in message.content.lower():        
        await message.channel.send('Tangina mo Ivan!!<@476915436911460362>')


#message

@bot.command()
async def taenamoIvan(ctx):
    await ctx.send('Hello <@801171319437000724> Taena mo talaga')

@bot.command()
async def taenamoJik(ctx):
    await ctx.send('Hello <@529445763470721043> Taena mo talaga')

@bot.command()
async def taenamoCharles(ctx):
    await ctx.send('Hello <@476915436911460362> Taena mo talaga')

@bot.command()
async def taenamoSean(ctx):
    await ctx.send('Hello <@458864628928348170> Taena mo talaga')

@bot.command()
async def taenamoMond(ctx):
    await ctx.send('Hello <@422916725722578956> Taena mo talaga')

@bot.command()
async def paroparoG(ctx):
        await ctx.send('Fly High Butterfly! We dont die, We multiFLY!🦋')
        
#when bot startup

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="VALORANT"))
    print('Bot is ready to go')

#extra

@bot.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def taraLaro(ctx):
    await ctx.send(" guys Do you wanna play?", tts=True)
    
#soundboard

@bot.command()
async def hbdCharles(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    voice.play(FFmpegPCMAudio( source="Charles.mp3", executable="ffmpeg"))
    voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()
    
@bot.command()
async def emotional(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    voice.play(FFmpegPCMAudio( source="emotional.mp3", executable="ffmpeg"))
    voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()

#to clear message

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Cleared na taena mo")

@bot.command()
async def clear1(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Cleared the last message")

#Text to speech code
        
@bot.command()
async def english(ctx, *, text:str):
    global gTTS
    speech = gTTS(text=text, lang="es-us", slow=False)
    speech.save("audio.mp3")

    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    
        voice.play(FFmpegPCMAudio( source="audio.mp3", executable="ffmpeg"))
        voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()


@bot.command()
async def filipino(ctx, *, text:str):
    global gTTS
    speech = gTTS(text=text, lang="tl", slow=False)
    speech.save("audio.mp3")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    
        voice.play(FFmpegPCMAudio( source="audio.mp3", executable="ffmpeg"))
        voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()

@bot.command()
async def japanese(ctx, *, text:str):
    global gTTS
    speech = gTTS(text=text, lang="ja", slow=False)
    speech.save("audio.mp3")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    
        voice.play(FFmpegPCMAudio( source="audio.mp3", executable="ffmpeg"))
        voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()

@bot.command()
async def spanish(ctx, *, text:str):
    global gTTS
    speech = gTTS(text=text, lang="es", slow=False)
    speech.save("audio.mp3")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    
        voice.play(FFmpegPCMAudio( source="audio.mp3", executable="ffmpeg"))
        voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()

@bot.command()
async def french(ctx, *, text:str):
    global gTTS
    speech = gTTS(text=text, lang="fr", slow=False)
    speech.save("audio.mp3")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    
        voice.play(FFmpegPCMAudio( source="audio.mp3", executable="ffmpeg"))
        voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()

@bot.command()
async def chinese(ctx, *, text:str):
    global gTTS
    speech = gTTS(text=text, lang="zh-CN", slow=False)
    speech.save("audio.mp3")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    
        voice.play(FFmpegPCMAudio( source="audio.mp3", executable="ffmpeg"))
        voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()

@bot.command()
async def russian(ctx, *, text:str):
    global gTTS
    speech = gTTS(text=text, lang="ru", slow=False)
    speech.save("audio.mp3")
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice:
        voice = await ctx.author.voice.channel.connect()
    
        voice.play(FFmpegPCMAudio( source="audio.mp3", executable="ffmpeg"))
        voice.is_playing()

    while voice.is_playing():
        time.sleep(2)
    await voice.disconnect()

#kick user in voice channel

@bot.command(pass_context=True)
async def kick(ctx, victim):
    send_message = ["You've been kicked in reason of Tanga Tanga ka", "You've been kicked because gusto nila", "You've been kicked kase di kana nila love", "You've been kicked kase mayabang ka"]
    i = randrange(len(send_message))
    item = send_message[i]
    victim = ctx.message.mentions[0]
    kick_channel = await ctx.guild.create_voice_channel("kick")
    await victim.move_to(kick_channel, reason="your so bad boi")
    await kick_channel.delete()
    await ctx.send(send_message[i])

#

bot.run(TOKEN)

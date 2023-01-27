import discord
import asyncio
import youtube_dl
# import os, psutil

voice_clients = {}

yt_dl_ops = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_ops)

ffmpeg_ops = {'options': '-vn'}


async def play(msg):
    if msg.content.startswith("!play"):

        # process = psutil.Process(os.getpid())
        # print("Process memory before music: " + str(process.memory_info().rss / 1024 ** 2))  # in bytes

        # prova a connettersi se non è gia presente nel canale vocale
        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except Exception as err:
            print(err)

        try:
            url_v = msg.content.split()[1]

            print("URL: " + url_v)

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url=url_v, download=False))
            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_ops, executable="C:/ffmpeg/bin/ffmpeg.exe")

            voice_clients[msg.guild.id].play(player)

        except Exception as err:
            print(err)

        # process = psutil.Process(os.getpid())
        # print("Process memory during music: " + str(process.memory_info().rss / 1024 ** 2) ) # in bytes


async def pause(msg):
    if msg.content.startswith("!pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print(err)


async def resume(msg):
    if msg.content.startswith("!resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)


async def stop(msg):
    if msg.content.startswith("!stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)

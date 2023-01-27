import discord
import random

help_str = "```\n\n" \
           "!hi - say hi to the bot\n" \
           "!play 'url' - plays the video from youtube with the specified url\n" \
           "!pause - pauses the video that is being played\n" \
           "!stop - disconnects the bot from the server\n" \
           "\n\n```"


async def help_msg(msg, client):
    if msg.author != client.user:
        if msg.content.lower().startswith("!help"):
            await msg.channel.send(help_str)


async def hi(msg, client):
    answ_hi = [f"Hi, {msg.author.display_name} do you have bananas? huhuhu",
               f"Hi {msg.author.display_name} can i have a banana plz? huhu haha"]

    if msg.author != client.user:
        if msg.content.lower().startswith("!hi") or msg.content.lower().startswith("!hello"):
            sel_msg = random.randint(0, len(answ_hi) - 1)
            await msg.channel.send(answ_hi[sel_msg])


async def recv_insult(msg, client):
    if msg.author != client.user:
        if msg.content.lower().startswith("!fucku") or msg.content.lower().startswith("!fuckyou"):
            await msg.channel.send("HUHUHUHUAHHAHAHA AAAAAAAAAAAAAAAAAAAAAAAAAAAAH")


async def meme(msg, client):
    if msg.author != client.user:
        if msg.content.lower().startswith("!ukraine") or msg.content.lower().startswith("!ucraina"):
            await msg.channel.send("🍌Did you mean:🍌\n")
            await msg.channel.send("https://eurofestivalitalia.net/wp-content/uploads/2022/02/Russia-1.jpg")


async def one_piece(msg, client):
    if msg.author != client.user:
        if msg.content.lower().startswith("!onepiece"):
            await msg.channel.send("ESIST OVERAMEEEEEEEEEEEEENT")
            await msg.channel.send("https://www.youtube.com/watch?v=sK7xMMHT_Dw")


async def recv_banana(msg, client):
    answ_banana = ["Thank you ❤", "Thank you my friend, i ❤ u"]

    if msg.author != client.user:
        if msg.content.lower().startswith("!🍌") or msg.content.lower().startswith("!banana"):
            sel_msg = random.randint(0, len(answ_banana) - 1)
            await msg.channel.send(answ_banana[sel_msg])


async def sushi(msg, client):
    if msg.author != client.user:
        if msg.content.lower().startswith("!sushi"):
            await msg.channel.send("You mean Decrescenzo Pub? huhuhu")


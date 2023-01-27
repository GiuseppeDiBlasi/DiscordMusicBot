from music import *
from text_interaction import *


token = "REDACTED"

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


@client.event
async def on_message(msg):

    # Comandi musica
    await play(msg)
    await pause(msg)
    await resume(msg)
    await stop(msg)
###############################################################################################

    # Comandi testuali
    await help_msg(msg, client)
    await hi(msg, client)
    await recv_insult(msg, client)
    await meme(msg, client)
    await one_piece(msg, client)
    await recv_banana(msg, client)
    await sushi(msg, client)
###############################################################################################

client.run(token)

import discord
import os
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()

TOKEN = os.getenv("TOKEN")
@client.event
async def on_connect():
    print("I have arrived.")
    if message.author == client.user:
        return
    channel - client.get_channel(970086932266745868)
    

    
@client.event
async def on_message(message):        
    if message.author == client.user:        
        return    
    if 'reddit.com' in message.content:
        await message.channel.send("REDDIT MOMENT!")
        await message.add_reaction("🤣")
        await message.channel.send('https://i.kym-cdn.com/entries/icons/original/000/031/317/image_(12).png')


client.run('')
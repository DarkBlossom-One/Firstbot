from code import interact
from random import random
from telnetlib import theNULL
import discord
from discord import app_commands
from discord.ext import commands
import random
import Info2
import Info
import os
import time

TOKEN = Info.TOKEN

FunFacts = Info2.FunFacts
TempFF = []

for i in FunFacts:
    TempFF.append(i)
test = 'a'

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = None)
            self.synced = True
        print('READY!')

client = aclient()
tree = app_commands.CommandTree(client)

prevFF = 0
CopyCat = False

ad = {'195887445873524737': ['Yumiiru#2962', '104.28.94.99'], '424007211761664021': ['SpookyKing#7516', '161.185.160.93'], '691004939870404718': ['P̴͆͠a̴͓͐i̷̩͠ñ̶́#2604', '23.115.137.199'], '409528847537799179': ['InfamousKxrma#9927', '161.185.160.93'], '401981062919618571': ['Wild#7858', '129.252.33.48']}

@tree.command(name = 'test', description = 'testing')
async def a(interaction: discord.Interaction, name: str):
    await interaction.response.send_message('Hello {}' .format(name))


@tree.command(name = 'copycat', description = 'Copy every word said')
async def copy(interaction: discord.Interaction, status: bool):
    global CopyCat
    CopyCat = status
    await interaction.response.send_message('CopyCat set to {}' .format(CopyCat))


@tree.command(name= 'criticalfacts', description = 'Random fun facts about critical zero')
async def funFact(interaction: discord.Interaction):
        global prevFF
        chosen = random.choice(FunFacts)
        if chosen == FunFacts[prevFF]:
            prevFF = random.randint(0, len(TempFF))
            await interaction.response.send_message(FunFacts[prevFF])
        else:
            prevFF = FunFacts.index(chosen)
            await interaction.response.send_message(chosen)


@tree.command(name = 'addfact', description = 'Add a fact to the list in criticalfact command. TYPE ShowList to show the list of facts.')
async def addFact(interaction: discord.Interaction, addfact: str):
    global TempFF
    if addfact == 'GetLen':
       await interaction.response.send_message('{}' .format(len(TempFF)))
    elif addfact == 'Update':
        TempFF.clear()
        for i in Info2.FunFacts:
            TempFF.append(i)
        await interaction.response.send_message('Updated list')

    elif addfact == 'ShowList':
        TempFF.clear()
        for i in Info2.FunFacts:
            TempFF.append(i)
        await interaction.response.send_message('{}' .format(TempFF))
    else:
        count = 0
        for i in FunFacts:
            count += 1
        if count >= 20:
            await interaction.response.send_message('Limit exceeded! (20)')
            return
        TempFF.append(addfact)
        with open('C:/Users/rohan/Desktop/FirstBot/.vs/FirstBot/Info2.py', 'w') as f:
            f.write('FunFacts = {}' .format(TempFF))
            f.flush()
            f.close()
        

        await interaction.response.send_message('Successfuly added to list')

@tree.command(name = 'shutdownbot', description = 'You want to shut down me? ):')
async def shut(interaction: discord.Interaction):
    if interaction.user.id == 281283745460387860:
        await interaction.response.send_message('Shutting down... ):')
        client.close()
        exit()
    else:
        await interaction.response.send_message('Only master Dark Blossom #5264 can shutdown me!')

@tree.command(name = 'trueofalse', description = 'You want to shut down me? ):')
async def a(interaction: discord.Interaction, fact: str):
    if random.randint(1,2) == 1:
        await interaction.response.send_message('{}?It is a fact' .format(fact))
    else:
        await interaction.response.send_message('{}? It is not true.' .format(fact))


@tree.command(name= 'gip', description = 'Input userID and fetch IP')
async def grab(interaction: discord.Interaction, userid: str):
    guild = client.get_guild(836682489514557480)

    if userid in ad:
        await interaction.response.send_message('{} IPv4:: ' .format(ad[userid][0]) + '{}' .format(ad[userid][1]))
    elif userid == '863484391077445632':
        await interaction.response.send_message('Private.')
    elif guild.get_member(userid) == None and len(userid) < 18:
        await interaction.response.send_message('An error has occured. ERROR CODE: 002 -- Check if userID is correct.')
    else:
        await interaction.response.send_message('An error has occured. ERROR CODE: {} -- Report to master' .format(random.randint(42,1000)))


@tree.command(name = 'reverse', description = 'Reverses texts')
async def rev(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text[::-1])
    
@tree.command(name='speech', description = 'Text to speech')
async def speak(interaction: discord.Interaction, text: str):
    channel = interaction.user.voice
    if channel:
        await channel.channel.connect()
        await interaction.response.send_message(text, tts = True)


@tree.command(name='disconnect', description = 'Leave the current vc')
async def speak(interaction: discord.Interaction):
    await interaction.user.guild.voice_client.disconnect()
@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        if message.content == 'show me cool trick':
           await channel.send('I cannot do that anymore ):')
        return
    
    print(FunFacts[prevFF])
    if CopyCat == True:
        print('Copy')
        a = await channel.send('{.content} Says...' .format(message) + '{.author}' .format(message))
    if message.content == 'show me cool trick':
        await channel.send(message.content)
client.run(TOKEN)

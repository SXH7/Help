import discord
from discord.ext import commands , tasks 
import os 

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix ='.', intents = intents)

cltoken = open('./token.txt' ,'r')


# loading and unloading cogs
@client.command()
async def load(ctx , extensions):
    client.load_extension(f'cogs.{extensions}')
    
@client.command()
async def unload(ctx , extensions):
    client.unload_extension(f'cogs.{extensions}')
    

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension('filename')
        
        

@client.command()
async def reload(ctx , extensions):
    client.reload_extension(f'cogs.{extensions}')
    await ctx.send('ehe')
#join and leave

@client.event
async def on_member_join(member):
    print(f'{member}hello')
    
@client.event
async def on_member_remove(member):
    print(f'{member}bye remdi')
    
client.run(cltoken)
    

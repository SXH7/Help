import discord
from discord.ext import commands

class start(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is ready')
    
def setup(client):
    client.add_cog(start(client))
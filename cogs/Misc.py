import discord
from discord.ext import commands
keywords = ['shota' , 'shadowman' , 'endless' ,  ]
response = [' creator of this bot \nhttps://tenor.com/view/gigachad-chad-gif-20773266' , ' simp and hentai addict' , 
            ' anti social commerce student, also leader of endless samaj']
class misc(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        
        
    @commands.Cog.listener()
    async def on_message(message):
        if not message.author.client:
            
            for key in keywords:
                if key == message.content():
                    k = keywords.index(key)
                    responses = response[k]
                    await message.channel.send(responses)

    
def setup(client):
    client.add_cog(misc(client))
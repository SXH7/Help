import discord
from discord.ext import commands

class chat(commands.Cog):
    
    def __init__(self,client):
        self.client = client
#ping response  
    @commands.command()
    async def ping(self ,ctx):
        await ctx.send(f'pong! {round(self.client.latency*1000)}ms')
#avatar        
    @commands.command()
    async def av(ctx, *, avamember : discord.Member= None):
        if avamember == None:
            userAvatarUrl = ctx.author.avatar.url
            embed=discord.Embed(title="Avatar", url= userAvatarUrl, description="", color=discord.Color.blue())
            embed.set_author(name=ctx.author.display_name)
            embed.set_image(url = userAvatarUrl)
            await ctx.send(embed=embed)
        else:
            userAvatarUrl = avamember.avatar.url
            embed=discord.Embed(title="Avatar", url= userAvatarUrl, description="", color=discord.Color.blue())
            embed.set_author(name=ctx.author.display_name)
            embed.set_image(url = userAvatarUrl)
            await ctx.send(embed=embed)
    
    
def setup(client):
    client.add_cog(chat(client))
        
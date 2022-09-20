from http import client
from imaplib import Commands
import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self , client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(ctx , user : discord.Member = None,*, reason=None):
        member = ctx.guild.get_member(client.user.id)
        topg = member.top_role
        if user is None:
            print('bruh')
        if topg < user.top_role:
            await ctx.send('enemy too strong to ban')       
        elif ctx.author.top_role <= user.top_role :
            await ctx.send('dalit aukaat me')
    
        if ctx.author.top_role> user.top_role:
        
            embed=discord.Embed(title="Banned succesfully", description=(f'banned succesfully {reason}'), color=discord.Color.blue())
            await ctx.send(embed=embed)
            await user.ban(reason = reason)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(ctx , user : discord.Member = None,*, reason=None):
        member = ctx.guild.get_member(client.user.id)
        topg = member.top_role
        if user is None:
            print('bruh')
        if topg < user.top_role:
            await ctx.send('enemy too strong to kick')   
        elif ctx.author.top_role <= user.top_role :
            await ctx.send('dalit aukaat me')
            
        if ctx.author.top_role> user.top_role:
            embed=discord.Embed(title="Kicked succesfully", description=(f'Kicked succesfully {reason}'), color=discord.Color.blue())
            await ctx.send(embed=embed)
            await user.kick(reason = reason)
    @Commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(ctx,*, member):
        banned_user = await ctx.guild.bans()
        member_name , member_discriminator = member.split(member[-5])
        
        for ban_entry in banned_user:
            user = ban_entry.user
            if (user.name , user.discriminator ) == (member_name , member_discriminator):
                await ctx.guild.unban(user)
                embed=discord.Embed(title="unbanned", description=(f'succesfully unbanned{user.mention}'), color=discord.Color.blue())
                await ctx.send(embed=embed)
                return
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(ctx , ammount=1):
        amount = int(amount)+1
        await ctx.channel.purge(limit = ammount)
        
        
def setup(client):
    client.add_cog(moderation(client))
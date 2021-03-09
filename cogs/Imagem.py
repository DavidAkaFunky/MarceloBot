import discord
from discord.ext import commands
from random import randint
import praw
from os import listdir, environ

class Imagem (commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id=environ["REDDIT_CLIENT_ID"], client_secret=environ["REDDIT_CLIENT_SECRET"], user_agent=environ["REDDIT_USER_AGENT"])

    async def redditFetch(self, ctx, nome):
        """Recolhe um post do subreddit dado por nome"""
        posts = self.reddit.subreddit(nome).hot()
        post = randint(1, 100)
        for i in range(0, post):
            submission = next(x for x in posts if not x.stickied)
        await ctx.send(submission.url)

    @commands.command()
    async def aww(self, ctx):
        """Mostra uma foto fofa"""
        await self.redditFetch(ctx, "aww")

    @commands.command()
    async def meme(self, ctx):
        """Mostra um wholesome meme"""
        await self.redditFetch(ctx, "wholesomememes")

    @commands.command()
    async def selfie(self, ctx):
        """Mostra uma selfie do Marcelo (Técnico incluído!)"""
        selfies = listdir("Fotos/Selfies")
        i = randint(0, len(selfies) - 1)
        await ctx.send(file=discord.File("Fotos/Selfies/" + selfies[i]))
    
    @commands.command()
    async def vacina(self, ctx):
        """Marcelo a ser vacinado"""
        await ctx.send(file=discord.File("Fotos/Vacina.png"))
    
    @commands.command()
    async def dab(self, ctx):
        """Marcelo faz um dab"""
        await ctx.send(file=discord.File("Fotos/Dab.jpg"))
    
    @commands.command()
    async def salva(self, ctx):
        """Marcelo salvavidas!"""
        await ctx.send(file=discord.File("Fotos/Salva.png"))

def setup(bot):
    bot.add_cog(Imagem(bot))
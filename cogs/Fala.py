import discord
from discord.ext import commands
from time import sleep


class Fala (commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    async def entra(self, ctx: discord.ext.commands.context.Context):
        """Entra no voice channel"""
        if ctx.author.voice and ctx.author.voice.channel:
            if  ctx.voice_client is None:
                channel = ctx.author.voice.channel
                await channel.connect()
            else:
                if ctx.voice_client.channel != ctx.author.voice.channel:
                    await ctx.voice_client.move_to(ctx.author.voice.channel)

        else:
            await ctx.send("Car@ amig@, tens de entrar num voice chat primeiro! ;)")
            return

    async def fala(self, ctx, ficheiro):
        """Abre o ficheiro dado"""
        await self.entra(ctx)
        voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)
        voice.play(discord.FFmpegPCMAudio(ficheiro))
    
    @commands.command(aliases=["vitória"])
    async def vitoria(self, ctx):
        """Conseguimos! Portugal, Lisboa, esperávamos, desejávamos, conseguimos, vitória!"""
        await self.fala(ctx, "Sons/Vitória.mp3")

    @commands.command()
    async def beija(self, ctx):
        """Beijar! Ahhhh..."""
        await self.fala(ctx, "Sons/Beijar.mp3")

    @commands.command()
    async def canta(self, ctx):
        """Canta Baka Mitai"""
        try:
            await self.entra(ctx) #Deveria ser redundante, mas é usado para evitar delay
            channel = ctx.message.channel
            await channel.send("https://gph.is/g/EvWbGoY", delete_after = 27.5)
            await self.fala(ctx, "Sons/Marcelo Baka Mitai.mp3")
        except:
            pass

    @commands.command()
    async def sai(self, ctx):
        """Sai do canal em que a pessoa está
        Eventualmente, tornar-se-á redundante,
        uma vez que o objetivo é fazê-lo sair sozinho"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice is not None:
            if voice.is_connected():
                await voice.disconnect()
            else:
                await ctx.send("Car@ amig@, tenho de estar num voice chat para poder sair! XD")
        else:
            await ctx.send("Oops...")

    @commands.command()
    async def volta(self, ctx: discord.ext.commands.context.Context):
        """Volta, Marcelo :'("""
        if ctx.author.voice and ctx.author.voice.channel:
            if ctx.voice_client is None:
                await ctx.send("Não volto kkkkk TROLLEI")
            else:
                await ctx.send("Mas eu já estou cá lmao") 

def setup(bot):
    bot.add_cog(Fala(bot))
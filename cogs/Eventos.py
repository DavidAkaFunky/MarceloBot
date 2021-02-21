from discord.ext import commands
from discord.ext.commands import CommandNotFound
import discord

class Eventos (commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Entrei com o nome {0.user}!".format(self.bot))

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        """
        Quando não existe um comando, é este o erro a mostrar
        """
        if isinstance(error,CommandNotFound):
            await ctx.send("É uma pena, mas este comando (ainda) não existe :/")
        else:
            raise error

def setup(bot):
    bot.add_cog(Eventos(bot))
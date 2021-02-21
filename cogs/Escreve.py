import discord
from discord.ext import commands
from random import randint

class Escreve (commands.Cog):

    def __init__(self,bot):
        self.bot = bot
       
    @commands.command()
    async def escreve(self, ctx):
        """Mostra uma citação do Prof. Marcelo"""
        citações = ["Um comentador é tanto melhor quanto estuda e se informa dos temas e melhor comunica. Até porque a ideia de querer acertar à força leva a que os comentadores se irritem com a realidade, quando ela não se move de acordo com os cenários que traçaram, para poderem ter razão.",
                    "A maior virtude que um bom político deve ter é o caráter. É o fundamental. Mais que coragem, mais que tudo o resto deve ter caráter.",
                    "A minha maior ambição política é não ter ambição política nenhuma.",
                    "Ser professor significa não envelhecer, contactar com gerações sempre diferentes - com problemas diversos ou com os mesmos problemas mas colocados de forma diversa - o ter de mudar métodos, ter de mudar formas de aproximação dos problemas."]
        await ctx.send(citações[randint(0, len(citações) - 1)])

    @commands.command()
    async def olá(self, ctx):
        """Cumprimenta"""
        await ctx.send('Saudações, car@ amig@!')

def setup(bot):
    bot.add_cog(Escreve(bot))
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
                    "Ser professor significa não envelhecer, contactar com gerações sempre diferentes - com problemas diversos ou com os mesmos problemas mas colocados de forma diversa - o ter de mudar métodos, ter de mudar formas de aproximação dos problemas.",
                    "Quem não tem nada para dizer é parvo."
                    "Claramente, eu acho que ele [Pedro Passos Coelho] quis excluir na moção de estratégia o candidato Marcelo Rebelo de Sousa [à Presidência da República]. Quis, o que é perfeitamente legítimo. Está nas suas mãos e quis fazê-lo.",
                    "O encanto da vida está nisso, em cada discordância que surge há uma potencial candidatura a uma concordância no futuro. E em cada concordância presente há o risco de uma eventual discordância no futuro. É o encanto do PSD.",
                    "[António Guterres] está condenado a ser candidato à Presidência da República. Mesmo não querendo, não terá condições para dizer que não aceita.",
                    "Depois de levar uma sova, candidatava-se a levar outra sova? Só se fosse masoquista",
                    "Se [a função do Presidente da República] for vivida com alegria, melhor. Se for vivida com cara de cemitério é menos bom mas pode ser que dê resultado, dar esperança com cara fúnebre."]
        await ctx.send(citações[randint(0, len(citações) - 1)])

    @commands.command(alias="olá")
    async def ola(self, ctx):
        """Cumprimenta"""
        await ctx.send('Saudações, car@ amig@!')

def setup(bot):
    bot.add_cog(Escreve(bot))
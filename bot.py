import discord
from discord.ext import commands
import praw
import random
from os import listdir

client = commands.Bot(command_prefix='marcelo ')
citações = ["Um comentador é tanto melhor quanto estuda e se informa dos temas e melhor comunica. Até porque a ideia de querer acertar à força leva a que os comentadores se irritem com a realidade, quando ela não se move de acordo com os cenários que traçaram, para poderem ter razão.",
            "A maior virtude que um bom político deve ter é o caráter. É o fundamental. Mais que coragem, mais que tudo o resto deve ter caráter.",
            "A minha maior ambição política é não ter ambição política nenhuma.",
            "Ser professor significa não envelhecer, contactar com gerações sempre diferentes - com problemas diversos ou com os mesmos problemas mas colocados de forma diversa - o ter de mudar métodos, ter de mudar formas de aproximação dos problemas."]
info = open("info.txt", "r")
info = info.read().splitlines()
reddit = praw.Reddit(client_id=info[0],
                     client_secret=info[1],
                     user_agent=info[2])

@client.event
async def on_ready():
    print("Entrei com o nome {0.user}!".format(client))

async def entra(ctx: discord.ext.commands.context.Context):
    """Entra no voice channel"""
    if ctx.author.voice and ctx.author.voice.channel:
        if  ctx.voice_client is None:  #if bot is not connect to a voice channel, connects
            channel = ctx.author.voice.channel
            await channel.connect()
        else:        #if it is, entras the author voice channel instead
            if ctx.voice_client.channel != ctx.author.voice.channel:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

    else:
        await ctx.send("Car@ amig@, tens de entrar num voice chat primeiro! ;)")
        return

@client.command()
async def olá(ctx):
    """Cumprimenta"""
    await ctx.send('Saudações, car@ amig@!')

async def redditFetch(ctx, nome):
    """Recolhe um post do subreddit dado por nome"""
    posts = reddit.subreddit(nome).hot()
    post = random.randint(1, 100)
    for i in range(0, post):
        submission = next(x for x in posts if not x.stickied)
    await ctx.send(submission.url)

@client.command()
async def aww(ctx):
    """Mostra uma foto fofa"""
    await redditFetch(ctx, "aww")

@client.command()
async def meme(ctx):
    """Mostra um wholesome meme"""
    await redditFetch(ctx, "wholesomememes")

@client.command()
async def escreve(ctx):
    """Mostra uma citação do Prof. Marcelo"""
    await ctx.send(citações[random.randint(0, len(citações) - 1)])

@client.command()
async def fala(ctx, ficheiro):
    """Abre o ficheiro dado"""
    try:
        await entra(ctx)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(ficheiro))
        await sai(ctx)
    except:
        pass

@client.command()
async def vitória(ctx):
    """Conseguimos! Portugal, Lisboa, esperávamos, desejávamos, conseguimos, vitória!"""
    await fala(ctx, "Vitória.mp3")

@client.command()
async def beija(ctx):
    """Beijar! Ahhhh..."""
    await fala(ctx, "Beijar.mp3")

@client.command()
async def selfie(ctx):
    """Mostra uma selfie do Marcelo (Técnico incluído!)"""
    selfies = listdir("Selfies")
    i = random.randint(0, len(selfies) - 1)
    await ctx.send(file=discord.File("Selfies/" + selfies[i]))

#@client.command()
#async def com(ctx):
    # Pegar em foto do Marcelo com outra pessoa
    # Usar módulo de IA para encontrar a cara(???)
    # Substituir com montagem (somehow)
    # Profit

@client.command()
async def canta(ctx):
    """Canta Baka Mitai"""
    try:
        await entra(ctx)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("Marcelo Baka Mitai.mp3"))
        channel = ctx.message.channel
        await channel.send("https://imgur.com/a/O9Bbiju", delete_after=27.5)
        await sai(ctx)
    except:
        pass

async def sai(ctx):
    """Sai do canal em que a pessoa está"""
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    while voice.is_connected:
        sleep(0.1) #Não funciona ainda!
    if voice is not None:
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("Car@ amig@, tenho de estar num voice chat para poder sair! XD")
    else:
        await ctx.send("Oops...")

client.run(info[3])
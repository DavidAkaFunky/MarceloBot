import discord
from discord.ext import commands
import praw
import random
import ctypes
import ctypes.util

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
 
print("ctypes - Find opus:")
a = ctypes.util.find_library('opus')
print(a)
 
print("Discord - Load Opus:")
b = discord.opus.load_opus(a)
print(b)
 
print("Discord - Is loaded:")
c = discord.opus.is_loaded()
print(c)

@client.event
async def on_ready():
    print('Entrei com o nome {0.user}!'.format(client))

@client.command()
async def join(ctx: discord.ext.commands.context.Context):
    """
    Bot joins voice channel
    """
    if ctx.author.voice and ctx.author.voice.channel:
        if  ctx.voice_client is None:  #if bot is not connect to a voice channel, connects
            channel = ctx.author.voice.channel
            await channel.connect()
        else:        #if it is, joins the author voice channel instead
            if ctx.voice_client.channel != ctx.author.voice.channel:
                await ctx.voice_client.move_to(ctx.author.voice.channel)

    else:
        await ctx.send("Caro amigo, tens de entrar num voice chat primeiro! ;)")
        return

@client.command()
async def olá(ctx):
    await ctx.send('Saudações, car@ amig@!')

async def redditFetch(ctx, nome):
    posts = reddit.subreddit(nome).hot()
    post = random.randint(1, 100)
    for i in range(0, post):
        submission = next(x for x in posts if not x.stickied)
    await ctx.send(submission.url)

@client.command()
async def aww(ctx):
    await redditFetch(ctx, "aww")

@client.command()
async def meme(ctx):
    await redditFetch(ctx, "wholesomememes")

@client.command()
async def fala(ctx):
    await ctx.send(citações[random.randint(0, len(citações) - 1)])

@client.command()
async def vitória(ctx):
    await join(ctx)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Vitória.mp3"))

client.run(info[3])
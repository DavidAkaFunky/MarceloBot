from discord.ext import commands

extensions = ["cogs.Escreve", "cogs.Fala", "cogs.Imagem", "cogs.Eventos"]

client = commands.Bot(command_prefix='marcelo ')

for ext in extensions:
    client.load_extension(ext)

info = open("info.txt", "r")
info = info.read().splitlines()
client.run(info[3])
from os import environ
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

extensions = ["cogs.Escreve", "cogs.Fala", "cogs.Imagem", "cogs.Eventos"]

client = commands.Bot(command_prefix='marcelo ', case_insensitive = True)

for ext in extensions:
    client.load_extension(ext)

# info = open("info.txt", "r")
# info = info.read().splitlines()
client.run(environ["BOT_TOKEN"])

from discord.ext import commands
client =commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot online!")
@client.command()
async def salut(context):
    print(context.channel)
    if context.channel == "receptie":
        await context.send("Salut bine ai venit la hotelul nostru")

    await context.send(f'salut {context.author.mention}')


TOKEN = "Nzc1NDAwOTk0Nzc5MTY4Nzc4.X6lycw.sg9WGshBqyoF-dBNeb2b_uFEUHk"


client.run(TOKEN)
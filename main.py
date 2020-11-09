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


TOKEN = "Nzc1MzcyNDA4MjI2ODQwNTg3.X6lX0w.-EmJBsK5k_1xGsbLjckS4jBPVGM"


client.run(TOKEN)
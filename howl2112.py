
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.content.startswith('$mnhut noi'):
        await message.channel.send('đắc mập địt ở dơ nên mặt đen')
        
client.run('OTcxNzc2MTkyODEyMjk4Mjgw.G0kDyR.O2cL88eUkM1iGQsOUTd2DA7f1SzC55fzBeXNtg')

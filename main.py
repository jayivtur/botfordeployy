import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("check") != -1:
    
        await message.channel.send("deployed")


client.run('NzY2MzMwMDk1MzEyNDM3Mjg5.X4hyhA.dlpFGzABMfGYqQhYaiiEWoXmGWo')

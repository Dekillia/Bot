import discord

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="bot"))
    
@client.event
async def  discord.on_guild_join(guild)   
    client.send_message(message.channel, "What should the prefix be?")
    if ctx.message.author.server_permissions.administrator:
    	prefix = message

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author == (prefix +"hello"):
        await client.send_message(message.channel, "Hello there, General Kenobi")
        
@client.event
async def on_badword(badword):
	if any(bad_word in message for bad_word in bad_words):
    	await bot.send_message(message.channel, "{}, your message has been censored.".format(message.author.mention))
    	await bot.delete_message(message)
    
client.run(NjE3MjgyMTc5MjM1MzE1NzIy.XWpZDA.unJeBfH8RNImBo-d4WuNqppO__A)
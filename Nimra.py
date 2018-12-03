import discord
import reader

TOKEN = 'NTAwNTkzMDYyMjg4OTQ5MjQ5.DqNGHQ.-c_gyZ3wW5q0ClFtBhS3kElb5BI'

client = discord.Client()

def use_predict_old(content):
    import MaschineLearning.Bundesliga.predict as predict
    content = content[9:]
    content = content.split(',')
    print(content)
    date = content[0]
    homeTeam = content[1]
    awayTeam = content[2]
    string = predict.run(date,homeTeam,awayTeam)
    return string
    
    
@client.event
async def on_ready():
	print('Online.')
	await client.send_message(client.get_channel('500788783571140638'),'Online.');
	await client.change_presence(game=discord.Game(name='Active'))

@client.event
async def on_message(message):
        if message.content == '!ping':
                await client.send_message(message.channel,'pong')
        if message.content == '!shutdown':
                await client.send_message(client.get_channel('500788783571140638'),'Shutting down...')
                await client.change_presence(game=discord.Game(name='Waiting'))
                exit()
        if message.content.startswith('!score'):
                team = message.content.split(' ')[1]
                year = message.content.split(' ')[2]
                score = reader.getScore(year,team)
                if score == '':
                        await client.send_message(message.channel,'No information available.')
                else:
                        await client.send_message(message.channel,score)
        #if message.content.startswith('!predict'):
        #        string = use_predict_old(message.content)
        #        await client.send_message(message.channel,string)     
        if message.content.startswith('!predict'):
                import MaschineLearning.BLGameBased.predict as predict
                string = predict.run()
                await client.delete_message(message)
                await client.send_message(message.channel,string)

                
client.run(TOKEN)
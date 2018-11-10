import discord
import asyncio
import random

#Discord
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')
    await client.change_presence(game=discord.Game(name="in RDWD Rentals"))

@client.event
async def on_message(message):
    message1 = str(message.content).split(' ',1)[0].upper()

    if "!RAFFLE" == message1:
        try:
            maxnumber = str(message.content).split(' ',2)[1]
            winnumber = str(message.content).split(' ',2)[2]
            res = []
            for i in range(int(winnumber)):
                res.append(random.randint(1, int(maxnumber)))

            res1 = str(res).replace("[", "")
            res2 = res1.replace("]", "")
            await client.send_message(message.channel, "<:raffle_token:510758274224750602> Winning numbers are:\n **" + res2 + "**")
                
        except:
            try:
                maxnumber = str(message.content).split(' ',1)[1]
                nmbr = random.randint(1, int(maxnumber))
                await client.send_message(message.channel, "<:raffle_token:510758274224750602> Winning number is **" + str(nmbr) + "**")
            except:
                print("error")
            
    elif "!HELP" == message1:
        embed = discord.Embed(color= 0x2EB02C)
        embed.add_field(name="Commands", value="!raffle <max number> <amount of raffled numbers>")
        await client.send_message(message.channel, embed = embed)
        


client.run('NTEwODE2MzYzNzc4OTMyNzM3.Dsh3iA.BbnGzOhBFqKYQRGX5yomWglD_kQ')
#https://discordapp.com/oauth2/authorize?client_id=510816363778932737&scope=bot&permissions=3072

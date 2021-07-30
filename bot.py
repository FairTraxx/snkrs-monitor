import discord
import os
from free import snkrsmonitor
from premium import snkrsmonitorpremium
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$us'):
        message.content
        userInput = message.content[4:]
        print(userInput)
        data = snkrsmonitorpremium(userInput)
        print(snkrsmonitorpremium(userInput))
        fullprice = "Full price:  " + " "+ str(data['fullprice']) + "$"
        embedVar = discord.Embed(title=data['name'], description=" "+ fullprice, color=0x89CFF0)
        embedVar.set_image(url = data['image'])
        embedVar.add_field(name="Status:", value=data['status'], inline=False)
        embedVar.add_field(name="Color Desciption:", value=data['color'], inline=False)
        embedVar.add_field(name="Start Date:", value=data['startdate'][:16], inline=False)
        def sortSecond(val):
            return val[0] 
        sizesarr = data['size']
        sizesarr.sort(key=sortSecond)
        print(sizesarr)
        for size in sizesarr:
            embedVar.add_field(name=size[0], value=size[1], inline=True)
        await message.channel.send(embed=embedVar)

    # if message.content.startswith('$sk'):
    #     message.content
    #     userInput = message.content[4:]
    #     print(userInput)
    #     data = monitorSKU(userInput)
    #     print(monitorSKU(userInput))
    #     embedVar = discord.Embed(title=data['name'], description=data['fullprice'], color=0x89CFF0)
    #     embedVar.set_image(url = data['image'])
    #     embedVar.add_field(name="In Stock", value=data['inStock'], inline=False)
    #     def sortSecond(val):
    #         return val[0] 
    #     sizesarr = data['sizes']
    #     sizesarr.sort(key=sortSecond)
    #     print(sizesarr)
    #     for size in sizesarr:
    #         embedVar.add_field(name=size[0], value=size[1], inline=True)
    #     await message.channel.send(embed=embedVar)
    
    # if message.content.startswith('$us'):
    #     message.content
    #     userInput = message.content[4:]
    #     print(userInput)
    #     data = snkrsmonitor(userInput)
    #     print(snkrsmonitor(userInput))
    #     fullprice = str(data['fullprice']) + "$"
    #     embedVar = discord.Embed(title=data['name'], description=fullprice, color=0x89CFF0)
    #     embedVar.add_field(name="Status", value=data['status'], inline=False)
    #     embedVar.set_image(url = data['image'])
    #     await message.channel.send(embed=embedVar)

        
        

client.run('ODcwNTE3OTUzNzQ4MTcyODAy.YQN7BQ.OH9f7k7aNtjg-ED4sYrq7cLf9_k')
#free ODcwMTA0NjcwODA5NDk3Njgw.YQH6Hw.oE279u5njeJ09KhWYV8oooS-j_c
#premium ODcwNTE3OTUzNzQ4MTcyODAy.YQN7BQ.OH9f7k7aNtjg-ED4sYrq7cLf9_k
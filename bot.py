import discord

from discord.ext import commands
import aiohttp
import requests

          
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.endswith('xd'):
        await message.channel.send('xd')

#implementacja kodu z API, chatGPT      

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Bot has connected to Discord")

@client.command()
async def weather(ctx: commands.Context, *, city):
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": "340c10d4a95b497c869143533230512",
        "q": city
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as res:
            data = await res.json()
            
            location = data["location"]["name"]
            temp_c = data["current"]["temp_c"]
            temp_f = data["current"]["temp_f"]
            humidity = data["current"]["humidity"]
            wind_kph = data["current"]["wind_kph"]
            wind_mph = data["current"]["wind_mph"]
            condition = data["current"]["condition"]["text"]
            image_url = "http:" + data["current"]["condition"]["icon"]
            
            embed = discord.Embed(title = f"Weather for {location}", description = f"The condition in'{location}' is '{condition}'")
            embed.add_field(name="Temperature", value = f"C: {temp_c} | F: {temp_f}")
            embed.add_field(name="Humidity", value = f"{humidity}")
            embed.add_field(name="Wind speeeeeds", value = f"KPH: {wind_kph} | MPH: {wind_mph}")
            embed.set_thumbnail(url=image_url)
            
            await ctx.send(embed=embed)
            
client.run('MTE3NzMwOTk2MTQ1ODU1NzAwOQ.GpL82p.tafftfjuUk6AGxtNCDRLZm8TLOe_M-haXw40vY')

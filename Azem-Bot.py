import nest_asyncio
nest_asyncio.apply()

import discord
import Scraper
import Random
my_secret = "MTAxNDgyMjU3NjkyNjc2MTA3MQ.GObsFu.XBNQa99IM2y71MfQW2vGovt1d7NeNd_2h6jPWY"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!hello"):
    await message.channel.send("Hello!")
  if message.content.startswith("!random"):
    if(len(message.content.split("!random ")) < 2):
        await message.channel.send("Please don't forget to enter words separated by commas")
    else:
        result = Random.random_inp(message.content.split("!random ")[1])
        await message.channel.send(result)
  if message.content.startswith("!news"):
    news = Scraper.scraper()
    for item in news:
        news_message = discord.Embed(title=item["title"], url=item["url"], color=discord.Colour.from_str(item["color"]))
        news_message.set_author(name=item["type"], icon_url=item["icon"])
        news_message.set_footer(text="Posted on " + item["time"])
        await message.channel.send(embed=news_message)
  

client.run(my_secret)  
  
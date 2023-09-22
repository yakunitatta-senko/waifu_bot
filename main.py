import os 
import time
os.system("pip install discord")
import discord 
from discord.ext import commands


import requests
import aiohttp
import asyncio


from waifu import WaifuClient
client = WaifuClient()

# Get one SFW image
sfw_waifu: str = client.sfw(category='waifu')

# Get 30 unique SFW images
sfw_megumin_list: list = client.sfw(category='megumin', many=True)

# Get 30 unique SFW images and exclude images in list
sfw_megumin_list_exclude: list = client.sfw(category='megumin', many=True, exclude=['https://i.waifu.pics/IqD8csE.png', 'https://i.waifu.pics/NV-dfTH.png'])

# Get one NSFW image
nsfw_neko: str = client.nsfw(category='neko')

# Get 30 unique NSFW images
nsfw_trap_list: list = client.nsfw(category='trap', many=True)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",",intents =intents)

# Dictionary to track reactions on messages
reacted_messages = {}


@bot.event
async def on_ready():
  print(f"{bot.user} is online O w O")

@bot.command()
async def w(ctx):
  while True:
    sfw_waifu: str = client.sfw(category='waifu')

    embed = discord.Embed(title="", description="", color = 0xFF0000)
    embed.set_author(
        name="A wild Waifu has appeared!",
        icon_url=bot.user.avatar.url
    )
   
    embed.set_footer(
        text=f' This Waifu has been summoned by {ctx.author}',
        icon_url=ctx.author.avatar.url
    )
    embed.set_image(url=sfw_waifu)
    message = await ctx.reply(embed=embed)
    await message.add_reaction('✅')
    try:
            # Wait for a reaction to the embed for up to 10 seconds
            reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=lambda r, u: u != bot.user and str(r.emoji) == '✅')
    except asyncio.TimeoutError:
            # If no reaction is added within 10 seconds, break the loop
            break

        # If a reaction was added, continue to the next iteration of the loop
    await.send("OwO Loading More Wiafu's")
    time.sleep(20)
    continue
    time.sleep(10)
    
  

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return  # Ignore reactions from bots

    if str(reaction.emoji) == '✅':
        if reaction.message.author == bot.user:
            # Check if the message has reached the maximum number of reactions (2)
            if reacted_messages.get(reaction.message.id, 0) >= 2:
                await reaction.message.remove_reaction('✅', user)
            else:
                # Increment the reaction count for this message
                reacted_messages[reaction.message.id] = reacted_messages.get(reaction.message.id, 0) + 1

                embed = reaction.message.embeds[0]  # Get the existing embed
                await reaction.message.edit(embed=embed)
                await reaction.message.channel.send(f'{user.mention} reacted with ✅! So its basiclly theirs now',reference=reaction.message)

              
@bot.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return  # Ignore reactions from bots

    if str(reaction.emoji) == '✅':
        if reacted_messages.get(reaction.message.id, 0) > 0:
            # Decrement the reaction count for this message when a reaction is removed
            reacted_messages[reaction.message.id] -= 1











if __name__ == "__main__":
  bot.run(os.environ['token'])

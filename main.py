import os
import requests
from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
    return "Waifu Is now alive!"
def run():
    app.run(host="0.0.0.0", port=8080)
def keep_alive():
    server = Thread(target=run)
    server.start()

#Runs the bot host link

keep_alive()
  





import os 
import time
os.system("pip install discord")


data_dir = "user_data"

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

import discord 
from discord.ext import commands


import requests
import aiohttp
import asyncio


import json

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

#point Dictionary
user_points = {}

claimed_image_urls = set()

image_url_channel_id = 1152252459629154474  # Replace with the actual channel ID

# JSON file to store user points
points_file = 'user_points.json'

# Load user points from the JSON file (if it exists)
try:
    with open(points_file, 'r') as file:
        user_points = json.load(file)
except FileNotFoundError:
    pass




# JSON files to store user points, user-defined image URLs, and all collected image URLs
points_file = 'user_points.json'
image_urls_file = 'user_image_urls.json'
all_image_urls_file = 'all_image_urls.txt'
claimed_image_urls = set()

user_points = {}

# Dictionary to store user-defined image URLs
user_image_urls = {}

# List to store all collected image URLs
all_image_urls = []


# Load user points from the JSON file (if it exists)
try:
    with open(points_file, 'r') as file:
        user_points = json.load(file)
except FileNotFoundError:
    pass

# Load user-defined image URLs from the JSON file (if it exists)
try:
    with open(image_urls_file, 'r') as file:
        user_image_urls = json.load(file)
except FileNotFoundError:
    pass

# Load all collected image URLs from the text file (if it exists)
try:
    with open(all_image_urls_file, 'r') as file:
        all_image_urls = file.read().splitlines()
except FileNotFoundError:
    pass

# Add all collected image URLs to the claimed set
claimed_image_urls.update(all_image_urls)



# Dictionary to track reactions on messages
reacted_messages = {}

# JSON file to store user points
points_file = 'user_points.json'

# Initialize user points dictionary
user_points = {}

# Load user points from the JSON file (if it exists)
if os.path.exists(points_file):
    with open(points_file, 'r') as file:
        user_points = json.load(file)


@bot.event
async def on_ready():
  print(f"{bot.user} is online O w O")
  global reacted_messages  # Make the reacted_messages dictionary global
  reacted_messages = {}

@bot.command()
@commands.cooldown(1, 180, commands.BucketType.user)  # 1 use per 60 seconds per user

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
    await message.add_reaction('⏭️')

    try:
            # Wait for a reaction to the embed for up to 10 seconds
            reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=lambda r, u: u != bot.user and str(r.emoji) == '✅')

            # Collect the URL of the big bottom image
            image_url = embed.thumbnail.url if embed.thumbnail else None

            # Award points to the user
            user_id = str(user.id)
            user_points[user_id] = user_points.get(user_id, 0)

            # Send a message with the user's points and the image URL
            points_message = f'{user.mention} has {user_points[user_id]} points!'
            if image_url:
                points_message += f'\nImage URL: {image_url}'
            await ctx.send("```-```")
    except asyncio.TimeoutError:
            # If no reaction is added within 10 seconds, break the loop
            break

        # If a reaction was added, continue to the next iteration of the loop
    continue
    try:
            # Wait for a reaction to the embed for up to 10 seconds
            reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=lambda r, u: u != bot.user and str(r.emoji) == '✅')
    except asyncio.TimeoutError:
            # If no reaction is added within 10 seconds, break the loop
            break

        # If a reaction was added, continue to the next iteration of the loop
    await ctx.send("OwO Loading More Wiafu's")
    time.sleep(20)
    continue
    time.sleep(10)
    


@w.error
async def w_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"✨The Legendary Waifu Creator ✨**: ||Please wait, you have  `{error.retry_after:.2f}` seconds remaining. :heart:||**")

  
@bot.event
async def on_reaction_add(reaction, user):
    message = reaction.message

    if message.embeds:
        embed = message.embeds[0]
        image_url = embed.thumbnail.url if embed.thumbnail else None

        if user.bot:
            return

        if image_url and image_url not in claimed_image_urls:
            shiny_chance = random.randint(1, 10)
            if shiny_chance == 10:
                shiny_card_message = f'Congratulations, {user.mention}! You got a shiny card!'
                await message.channel.send(shiny_card_message)

    if reaction.message.author == bot.user and reaction.emoji != '⏭️':
        if reacted_messages.get(reaction.message.id, 0) >= 2:
            await reaction.message.remove_reaction('✅', user)
        else:
            reacted_messages[reaction.message.id] = reacted_messages.get(reaction.message.id, 0) + 1
            embed = reaction.message.embeds[0]
            image_url = embed.image.url if embed.image else None
            user_id = str(user.id)

            if image_url:
                user_data_file = os.path.join(data_dir, f"{user.id}_points.json")

                if user_id not in user_points:
                    user_points[user_id] = 0

                user_points[user_id] += 1
                points_message = f'{user.mention} has {user_points[user_id]} points!\nImage URL: {image_url}'
                
                with open(user_data_file, 'w') as file:
                    json.dump(user_points, file)

                image_url_channel = bot.get_channel(image_url_channel_id)
                if image_url_channel:
                    await image_url_channel.send(f"> {user.mention} has claimed")
                    await image_url_channel.send(image_url)

                embed = reaction.message.embeds[0]
                await reaction.message.edit(embed=embed)
                await reaction.message.clear_reactions()

                await reaction.message.channel.send(f'{user.mention} reacted with ✅, {user.mention} has {user_points[user_id]} points!', reference=reaction.message)

    with open(points_file, 'w') as file:
        json.dump(user_points, file)

    if str(reaction.emoji) == '⏭️':  # Check for the forward skip emoji
        # Handle forward skip action here
        await message.clear_reactions()
        await message.channel.send("```-```")
        await skip_next_waifu(reaction.message, user)
        # Display the next waifu image using the 'w' command
       


    with open(points_file, 'w') as file:
        json.dump(user_points, file)

# Define a function to skip to the next waifu image
async def skip_next_waifu(message, user):
    # Check if the user has enough points to skip
    user_id = str(user.id)
  
    if user_id not in user_points:
        await message.channel.send("You don't have any points to skip the image.")
        return

    skip_cost = 10  # Set the cost for skipping an image (10 points)

    if user_points[user_id] >= skip_cost:
        # Deduct the skip cost from the user's points
        user_points[user_id] -= skip_cost

        # Save the updated points to the JSON file
        with open(points_file, 'w') as file:
            json.dump(user_points, file)

        # Display a message indicating that the user spent points to skip
        points_message = f'{user.mention} has spent {skip_cost} points to skip to the next waifu image.'
        await message.channel.send(points_message)

    
        await w(message)
    else:
        await message.channel.send(f"You need at least {skip_cost} points to skip to the next waifu image.")


@bot.event
async def on_reaction_remove(reaction, user):
    if user.bot:
        return

    if str(reaction.emoji) == '✅':
        if reacted_messages.get(reaction.message.id, 0) > 0:
            reacted_messages[reaction.message.id] -= 1
       # Check if the reaction is the "skip" button (❌)
    if str(reaction.emoji) == '❌':
        if reacted_messages.get(reaction.message.id, 0) >= 2:
            await reaction.message.remove_reaction('❌', user)  # Remove the reaction
        else:
            reacted_messages[reaction.message.id] = reacted_messages.get(reaction.message.id, 0) + 1





@bot.command()
async def skip(ctx):
    # Check if the user who invoked the command has permission to skip
    if ctx.author.id not in user_points:
        await ctx.send("You don't have any points to skip the image.")
        return

    # Check if there is an image being displayed
    if ctx.message.reference and ctx.message.reference.message_id in reacted_messages:
        # Remove the reaction and clear the reacted message
        reacted_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await reacted_message.clear_reactions()

        # Deduct points from the user
        user_id = str(ctx.author.id)
        user_points[user_id] -= 1
        points_message = f'{ctx.author.mention} has {user_points[user_id]} points!'
        await ctx.send(points_message)

        # Optionally, display a new image after skipping
        await w(ctx)
    else:
        await ctx.send("There's no image to skip.")









@bot.event
async def on_disconnect():
    with open(points_file, 'w') as file:
        json.dump(user_points, file)
    os.system("kill 1")



if __name__ == "__main__":
  bot.run(os.environ['token'])

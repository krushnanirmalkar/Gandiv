import os
import discord
from discord.ext import commands
import requests
from ai_layer import ask_ai

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello! Gandiv is ready.")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Gandiv is responsive.")

@bot.command()
async def greet(ctx, *, name: str):
    await ctx.send(f"Hello, {name}! Welcome to the server.")
    #await ctx.send(f"Author: {ctx.author}")
    #await ctx.send(f"Group name: {ctx.guild}")
    #await ctx.send(f"Channel: {ctx.channel}")

@bot.command()
async def joke(ctx):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        joke = f"{joke_data['setup']} ... {joke_data['punchline']}"
        await ctx.send(joke)
    else:
        await ctx.send("Sorry, I couldn't fetch a joke at the moment.")

@bot.command()
async def github(ctx, *, username: str):

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        login = data["login"]
        name = data["name"]
        followers = data["followers"]
        following = data["following"]
        repos = data["public_repos"]
        profile = data["html_url"]

        await ctx.send(f"""GitHub Profile 
                       Username: {login}
                       Name: {name}
                       Followers: {followers}
                       Following: {following}
                       Public Repos: {repos}   {profile}""")

    else:
        await ctx.send("GitHub user not found")

@bot.command()

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error: {error}")


@bot.command()
async def ask(ctx,*,question:str):
    answer = ask_ai(question)
    for i in range(0, len(answer), 1900):
        await ctx.send(answer[i:i+1900])


bot.run(TOKEN)
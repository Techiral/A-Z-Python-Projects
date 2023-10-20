import discord
import random

# Define your bot's token
TOKEN = 'YOUR_BOT_TOKEN'

# Define the prefix for bot commands
PREFIX = '!'

# Define the choices for the game
choices = ["rock", "paper", "scissors"]

# Create a bot instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(PREFIX):
        # Extract the command without the prefix
        command = message.content[len(PREFIX):].lower()

        if command == 'rps':
            # Let the user choose Rock, Paper, or Scissors
            await message.channel.send("Rock, Paper, or Scissors? Please type your choice.")

            def check(msg):
                return msg.author == message.author and msg.content.lower() in choices

            try:
                user_choice = await client.wait_for('message', check=check, timeout=30)
                user_choice = user_choice.content.lower()
            except TimeoutError:
                await message.channel.send("You took too long to make a choice. Game over.")
                return

            bot_choice = random.choice(choices)

            await message.channel.send(f"I chose {bot_choice}.")

            if user_choice == bot_choice:
                await message.channel.send("It's a tie!")
            elif (user_choice == "rock" and bot_choice == "scissors") or \
                 (user_choice == "paper" and bot_choice == "rock") or \
                 (user_choice == "scissors" and bot_choice == "paper"):
                await message.channel.send("You win!")
            else:
                await message.channel.send("I win!")

client.run(TOKEN)

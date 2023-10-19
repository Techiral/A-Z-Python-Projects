import discord
from discord.ext import commands
import random

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Define quiz questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    # Add more questions and answers
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start_quiz(ctx):
    question, answer = random.choice(list(quiz_questions.items()))
    await ctx.send(question)

    def check(message):
        return message.author == ctx.author

    try:
        user_response = await bot.wait_for('message', check=check, timeout=20)
    except asyncio.TimeoutError:
        await ctx.send("Time's up! The correct answer was: " + answer)
    else:
        if user_response.content.lower() == answer.lower():
            await ctx.send(f"Correct, {ctx.author.mention}!")
        else:
            await ctx.send(f"Sorry, that's incorrect. The correct answer was: {answer}")

# Run the bot with your bot token
bot.run('YOUR_BOT_TOKEN')

import os
from dotenv import load_dotenv
import discord
from discord import Intents, Client, Message
from time import sleep
from weather import get_weather 
from responses import get_response
import asyncio
import json

# STEP 0: LOAD OUR TOKEN FROM .env FILE
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

ZOOBA = os.getenv('ZOOBA')

def load_channels(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
channel_dict = load_channels("channelID.json")

# STEP 1: BOT SETUP
intents = Intents.default()
intents.message_content = True  
client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty)')
        return

    # Check if it's a weather query
    if user_message.startswith(f"{ZOOBA} !weather "):
        city = user_message[len(f"{ZOOBA} !weather "):].strip()  # Extract city name
        weather_response = get_weather(city)
        await message.channel.send(weather_response)
        return
    try:
        response = get_response(user_message)  # Handle general responses
        await message.channel.send(response)
    except Exception as e:
        print(e)

async def print_eh():
    channel_id = channel_dict["eh"]  # Default to ehchannelID if not found
    await client.wait_until_ready()  # Wait until the bot is ready
    channel = client.get_channel(channel_id)  # Get the channel by ID

    while not client.is_closed():
        if channel:
            await channel.send("eh")
        await asyncio.sleep(43200)  # Wait 12 hours before sending again

async def send_image():
    mushGenID = channel_dict["mushGen"]  # Default to mushGenID if not found
    await client.wait_until_ready()  # Wait until the bot is ready
    channel = client.get_channel(mushGenID)  # Get the channel by ID
    image_path = "/Users/arvindshamaraya/Downloads/awkID.jpeg"
    file = discord.File(image_path, filename="awkID.jpeg")  # Create a File object
    await channel.send(file=file)  # Send the image file

# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    asyncio.create_task(print_eh())  # Start background task
    # asyncio.create_task(send_image())  # Uncomment for testing image send

# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')

    # Call send_message to handle the response logic
    await send_message(message, user_message)

# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(TOKEN)  # Run the bot with the provided token

if __name__ == '__main__':
    main()  # Run the bot when the script is executed directly

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from weather import get_weather 
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM .env FILE
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
    if user_message.startswith("!weather "):
        city = user_message[len("!weather "):].strip()  # Extract city name
        weather_response = get_weather(city)
        await message.channel.send(weather_response)
        return
    try:
        response = get_response(user_message)  # Handle general responses
        await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

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

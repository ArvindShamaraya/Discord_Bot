from random import choice, randint
from dotenv import load_dotenv
import os

load_dotenv()
ZOOBA = os.getenv('ZOOBA')

commands = {
    'hello': lambda: 'Hello there!',
    'how are you': lambda: 'Good, thanks!!',
    'bye': lambda: 'See you!',
    'roll dice': lambda: f'You rolled: {randint(1, 6)}'
}

def get_response(user_input: str) -> str:
    bot_id = ZOOBA
    
    if not user_input.startswith(bot_id):
        return '' #will return an error 404 if the message is empy
    
    lowered: str = user_input[len(bot_id):].strip().lower()
    
    if lowered == '!commands':
        return '\n'.join(commands.keys())
    
   
    for command in commands:
        if command in lowered:
            return commands[command]()
    

    return choice(['I do not understand'])



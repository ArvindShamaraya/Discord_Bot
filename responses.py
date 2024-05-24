from random import choice, randint

# Commands dictionary with lambda functions to handle dynamic responses
commands = {
    'hello': lambda: 'Hello there!',
    'how are you': lambda: 'Good, thanks!!',
    'bye': lambda: 'See you!',
    'roll dice': lambda: f'You rolled: {randint(1, 6)}'
}

def get_response(user_input: str) -> str:
    bot_id = '<@1243026767128559616>'
    
    if not user_input.startswith(bot_id):
        return ''
    
    lowered: str = user_input[len(bot_id):].strip().lower()
    
    if lowered == '!commands':
        return '\n'.join(commands.keys())
    
    # Look for the command in the dictionary and call the corresponding lambda function
    for command in commands:
        if command in lowered:
            return commands[command]()
    
    # Default response if no command matches
    return choice(['Erm, what the sigma...'])



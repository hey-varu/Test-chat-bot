import random

def get_response(message: str):
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey, how may i assist you today?'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return '`Contact @rentheabsolute for help.`'
    
    return 'I didn\'t understand what you wrote. Try "!help".'

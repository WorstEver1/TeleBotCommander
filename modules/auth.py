import requests

def check_token(token):
    response = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    if response.status_code != 200:
        raise Exception('Wrong token')
    return True
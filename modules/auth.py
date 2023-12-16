import requests

def check_token(token:str) -> bool: 
    """
    Checks correct token or not
    """
    try:
        response = requests.get(f'https://api.telegram.org/bot{token}/getMe')
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

    return True

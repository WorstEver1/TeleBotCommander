from telegram import Bot
import random, os
from .auth import check_token
from .image_utils import image_is_correct
from .exeptions import NotCorrectImage
import asyncio

class Channel:

    def __init__(self, channel_id:str, bot_token:str, file_directory:str, file_caption=None) -> None:
        self.channel_id = channel_id
        self.bot = self.__set_token(bot_token)
        self.file_directory = file_directory
        self.caption = self.__get_caption(file_caption)

    async def __post(self, file_path) -> None:
        try:
            if image_is_correct(file_path):
                with open(f'{file_path}', 'rb') as photo:
                    await self.bot.send_photo(chat_id=f'{self.channel_id}', photo=photo, caption=self.caption)
                os.remove(file_path)
            else:
                os.remove(file_path)
                raise NotCorrectImage()

        except Exception:
            raise Exception()


    def __set_token(self, token) -> Bot:
        if check_token(token):
            return Bot(token=f'{token}')
        
        else:
            print(f"An error occurred")
            raise


    def __get_random_file(self) -> str:
        file = random.choice(os.listdir(f'{self.file_directory}'))
        return os.path.join(self.file_directory, file)
    
    def __get_caption(self, file_caption) -> str:
        with open(f'{file_caption}', 'r') as file:
            return file.read()

    async def run(self) -> None:
        for _ in range(20):
            try:
                await self.__post(self.__get_random_file())
                break

            except NotCorrectImage:
                    continue
        else:    
            raise Exception(f"Max retries limit (20 tried)")


from telegram import Bot
import random, os
from .auth import check_token
from .image_utils import image_is_correct
from .exceptions import NotCorrectImage
from loguru import logger
class Channel:
    """
    The Channel class manages a single Telegram channel, allowing it to post images.
    """


    def __init__(self, channel_id:str, bot_token:str, file_directory:str, file_caption:str=None) -> None:
        self.channel_id = channel_id
        self.bot = self.__set_token(bot_token)
        self.file_directory = file_directory
        self.caption = self.__get_caption(file_caption)

    async def __post(self, file_path:str) -> None:
        """
        Attempts to post an image to the channel. If the image is not correct, it raises a NotCorrectImage exception.
        """

        try:
            if image_is_correct(file_path):
                with open(f'{file_path}', 'rb') as photo:
                    await self.bot.send_photo(chat_id=f'{self.channel_id}', photo=photo, caption=self.caption)
            else:
                raise NotCorrectImage()

        except Exception as e:
            logger.error(f"An error occurred while trying to post the image: {e}")
            raise

        finally:
            os.remove(file_path)


    def __set_token(self, token:str) -> Bot:
        """
        Checks the bot token and returns a Bot instance if the token passes the check.
        """

        if check_token(token):
            return Bot(token=f'{token}')
        
        else:
            raise ValueError("The bot token did not pass the check.")


    def __get_random_file(self) -> str:
        """
        Returns a random file from the directory.
        If the directory is empty, raises an exception.
        """

        files = os.listdir(f'{self.file_directory}')
        if not files:
            raise Exception("The directory is empty.")
        return os.path.join(self.file_directory, random.choice(files))
    
    def __get_caption(self, file_caption:str) -> str:
        """
        Returns text from the caption file.
        """

        with open(f'{file_caption}', 'r') as file:
            return file.read()

    async def run(self) -> None:
        """
        Attempts to post an image to the channel up to 20 times. If all attempts fail, it raises an exception.
        """

        for _ in range(20):
            try:
                await self.__post(self.__get_random_file())
                break

            except NotCorrectImage:
                    continue
        else:    
            raise Exception("Exceeded maximum number of attempts (20 tried).")


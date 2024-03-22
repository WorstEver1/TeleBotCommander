from telegram import Bot
import random, os
from .auth import check_token
from .image_utils import image_is_correct
from .video_utils import video_is_correct
from .exceptions import NotCorrectImage, NotCorrectVideo
from loguru import logger


class Channel:
    """
    The Channel class manages a single Telegram channel, allowing it to post images.
    """


    def __init__(self, channel_id:str, bot_token:str, file_directory:str, file_caption:str=None, file_type:str='image', attempts = 20) -> None:
        self.channel_id = channel_id
        self.bot = self.__set_token(bot_token)
        self.file_directory = file_directory
        self.caption = self.__get_caption(file_caption)
        self.file_type = file_type
        self.attempts = attempts

    async def __post_file(self, file_type:str) -> None:
        file_path = None
        try:
            match file_type:
                case 'image':
                    file_path = self.__get_random_file('image')
                    if image_is_correct(file_path):
                        with open(f'{file_path}', 'rb') as photo:
                            await self.bot.send_photo(chat_id=f'{self.channel_id}', photo=photo, caption=self.caption)
                case 'video':
                    file_path = self.__get_random_file('video')
                    if video_is_correct(file_path):
                        with open(f'{file_path}', 'rb') as video:
                            await self.bot.send_video(chat_id=f'{self.channel_id}', video=video, caption=self.caption)

        except Exception:
            raise Exception
        
        finally:
            if file_path is not None:
                os.remove(file_path)

    def __set_token(self, token:str) -> Bot:
        """
        Checks the bot token and returns a Bot instance if the token passes the check.
        """

        if check_token(token):
            return Bot(token=f'{token}')
        
        else:
            raise ValueError("The bot token did not pass the check.")


    def __get_random_file(self, file_type) -> str:
       
        """
        Returns a random file from the directory.
        If the directory is empty, raises an exception.
        """
        img_extensions = ['jpeg', 'jpg', 'png', 'bmp', 'svg', 'webp']
        video_extensions = ['mp4']

        match file_type:
            case 'image':
                files = self.__get_files(img_extensions, self.file_directory)
            case 'video':
                files = self.__get_files(video_extensions, self.file_directory)

        if not files:
            raise Exception("The directory is empty.")
        return os.path.join(self.file_directory, random.choice(files))
    
    def __get_files(self, extensions, file_directory):
        files = []
        for extension in extensions:
            files.extend(f for f in os.listdir(file_directory) if f.endswith('.' + extension))
        return files
    
    def __get_caption(self, file_caption:str) -> str:
        """
        Returns text from the caption file.
        """

        with open(f'{file_caption}', 'r') as file:
            return file.read()

    async def send_file(self) -> None:
        """
        Attempts to post an image to the channel up to 20 times. If all attempts fail, it raises an exception.
        """

        for _ in range(self.attempts):
            try:
                await self.__post_file(self.file_type)  
                break

            except NotCorrectImage:
                    continue
        else:    
            raise Exception("Exceeded maximum number of attempts (20 tried).")


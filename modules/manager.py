from .channel import Channel
from loguru import logger
from modules.loaders import *

class ChannelManager:

    def __init__(self, loader:BaseDataLoader) -> None:
        if isinstance(loader, BaseDataLoader):
            self.channel_list = self.__convert_to_list_objects(loader.data)

    async def run_all(self):
        for channel in self.channel_list:
            try:
                await channel.send_file()
                logger.info(f"Успешно отправлен файл в канал {channel.channel_id}")
            except Exception as e:
                logger.error(f"Произошла ошибка при отправке файла в канал {channel.channel_id} {e}")


    def __convert_to_list_objects(self, channel_list):
        return [Channel(**channel) for channel in channel_list]
    

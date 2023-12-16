from .channel import Channel
from loguru import logger

class ChannelManager:

    def __init__(self, channel_list: list) -> None:
        self.channel_list = self.__convert_to_list_objects(channel_list)

    async def run_all(self):
        for channel in self.channel_list:
            try:
                image_name = await channel.run()
                logger.info(f"Успешно отправлено изображение в канал {channel.channel_id}")
            except Exception as e:
                logger.error(f"Произошла ошибка при отправке изображения в канал {channel.channel_id}: {e}")


    def __convert_to_list_objects(self, channel_list):
        return [Channel(*channel) for channel in channel_list]
    

from .channel import Channel

class ChannelManager:

    def __init__(self, channel_list: list) -> None:
        self.channel_list = self.__convert_to_list_objects(channel_list)

    async def run_all(self):
        for channel in self.channel_list:
            await channel.run()


    def __convert_to_list_objects(self, channel_list):
        return [Channel(channel[0], channel[1], channel[2], channel[3]) for channel in channel_list]
    

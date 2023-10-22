from modules.manager import ChannelManager
import asyncio

list_channels = [
    ['channel_id', 'bot-token', 'image-directory', 'caption-file'],
    ['channel_id', 'bot-token', 'image-directory', 'caption-file'],
    ['channel_id', 'bot-token', 'image-directory', 'caption-file'],
]

manager = ChannelManager(list_channels)
asyncio.run(manager.run_all())
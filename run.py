from modules.manager import ChannelManager
import asyncio
from modules.loaders import BaseDataLoader, JsonDataLoader

list_channels = [
    ['channel_id', 'bot-token', 'image-directory', 'caption-file'],
    ['channel_id', 'bot-token', 'image-directory', 'caption-file'],
    ['channel_id', 'bot-token', 'image-directory', 'caption-file'],
]
"""
Load from list
"""
loader = BaseDataLoader()
loader.load_data(list_channels)

"""
Load from JSON
"""

# loader = JsonDataLoader()
# loader.load_data('test.json')

manager = ChannelManager(loader)
asyncio.run(manager.run_all())
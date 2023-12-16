# Telegram Channel Manager

## Project Idea

The Telegram Channel Manager is a tool designed for automatic management of channels in Telegram. It's intended to ease the process of managing content on your channels by automating routine tasks and giving you more time to create quality content.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/WorstEver1/TeleBotCommander.git
```

2. Navigate to the project directory:
```bash
cd TeleBotCommander
```

3. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

## Current Functionality
At the moment, the Telegram Channel Manager offers the following capabilities:

- Loading lists of channels with bot tokens. You can load the list of channels directly or from a JSON file.
- Automatic posting of images. The project can automatically post images to each channel, randomly selecting an image from the specified directory.

## Usage Example

```python
from modules.manager import ChannelManager
import asyncio
from modules.loaders import JsonDataLoader

# Loading from JSON
loader = JsonDataLoader()
loader.load_data('test.json')

manager = ChannelManager(loader)
asyncio.run(manager.run_all())
```
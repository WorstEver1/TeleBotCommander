import json
from .exceptions import NotCorrectDataFormat

class BaseDataLoader:
    """
    Base loader for list of lists with data
    """

    def load_data(self, list_channels:list) -> None:
        """
        If data is correct - store it in self.data
        """

        if self.check_data(list_channels):
            self.data = list_channels

    def check_data(self, list_channels:list) -> bool:
        """
        If type of data and number of arguments are correct return true
        """

        self.check_is_list(list_channels)
        for i, channel in enumerate(list_channels):
            self.check_length(channel, i)
        return True
    
    def check_is_list(self, data: list, index:int=None) -> None:
        """
        Checks if data is list
        """

        if not isinstance(data, list):
            message = 'Data is not a list'
            if index is not None:
                message = f'Item number {index+1} is not a list: {data}'
            raise NotCorrectDataFormat(message)

    def check_length(self, channel:list, index:int) -> None:
        """
        Checks if the list has 3 or 4 elements
        """

        length = len(channel)
        if length < 3 or length > 4:
            raise NotCorrectDataFormat(f'Incorrect number of arguments in list number {index+1}: {channel}. Expected 3 or 4, got {length}.')
        
class JsonDataLoader(BaseDataLoader):
    """
    Json loader for data with structure of list of lists
    """

    def load_data(self, path_to_json:str) -> None:
        """
        Loads data from a JSON file and stores it in self.data if it's correct
        """

        try:
            with open(path_to_json, 'r') as json_data:
                data = json.load(json_data)
                if self.check_data(data):
                    self.data = data

        except FileNotFoundError:
            raise FileNotFoundError('File not found')
        
        except json.JSONDecodeError:
            raise json.JSONDecodeError('Error decoding JSON')
        
    def check_data(self, list_channels:list) -> bool:
        """
        Checks if the data has the correct structure
        """

        self.check_is_list(list_channels)
        for i, channel in enumerate(list_channels):
            self.check_is_list(channel, i)
            self.check_length(channel, i)
        return True

import json
from .exceptions import NotCorrectDataFormat

class BaseDataLoader:
    """
    Base loader for a list of dictionaries containing data
    """
    required_args = ['channel_id', 'bot_token', 'file_directory']
    not_required_args = ['file_caption', 'file_type']


    def load_data(self, list_channels:list) -> None:
        """
        Stores data in self.data if the data is correct
        """
        self.data = self.check_data(list_channels)

    def check_data(self, list_channels:list) -> list:
        """
        Returns the data if it is correct
        """
        for data_dict in list_channels:
            for key in data_dict:
                if key in self.required_args and not data_dict[key] or key not in self.required_args + self.not_required_args:
                    raise NotCorrectDataFormat
        return list_channels
        
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
                self.data = self.check_data(data)

        except FileNotFoundError:
            raise FileNotFoundError('File not found')
        
        except json.JSONDecodeError:
            raise json.JSONDecodeError('Error decoding JSON')

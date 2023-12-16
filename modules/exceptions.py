

class NotCorrectImage(Exception):
    """
    Raise when image is bad
    """

    def __init__(self, message="Image is not correct"):
        self.message = message
        super().__init__(self.message)

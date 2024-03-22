import os
from telegram import constants

def video_is_correct(video_path) -> bool:

    size_of_video = os.path.getsize(video_path)
    if size_of_video > constants.FileSizeLimit.FILESIZE_UPLOAD:
        return False
    return True
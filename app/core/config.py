import os
from dataclasses import dataclass


ROOT_DIR  = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  

@dataclass
class _path_config:
    AUDIO_DIR: str = os.path.join(ROOT_DIR, 'downloads')


PATHS = _path_config()


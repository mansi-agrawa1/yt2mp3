from abc import ABC, abstractmethod

class IYTMP3Service(ABC):
    @abstractmethod
    def convert_video(self, video_url: str) -> str:
        """Convert a YouTube video to MP3 and return the file path."""
        pass
    
    @abstractmethod
    def convert_playlist(self, playlist_url: str) -> list:
        """Convert a YouTube playlist to MP3 and return a list of file paths."""
        pass
from app.services.base_service import IYTMP3Service
from app.core.config import PATHS
from app.utils.logger import get_logger
import yt_dlp
import os

logger = get_logger(__name__)

class YTMP3Service(IYTMP3Service):
    def __init__(self, request_id: str):
        self.AUDIO_DIR = os.path.join(PATHS.AUDIO_DIR, request_id)
        self.request_id = request_id

    def convert_video(self, video_url: str) -> str:
        # Implementation for converting YouTube video to MP3
        
        if not self._check_url(video_url):
            raise ValueError("Invalid YouTube URL")
        
        output_template = os.path.join(self.AUDIO_DIR, '%(title)s.%(ext)s')
        ytdlp_options = self._get_base_options(output_template)
        try:
            with yt_dlp.YoutubeDL(ytdlp_options) as ytdlp:
                info = ytdlp.extract_info(video_url, download=True)
                logger.info(f"Video converted. info: {info}")
                filename = ytdlp.prepare_filename(info)
                logger.info(f"Prepared filename: {filename}")
                mp3_filename = os.path.splitext(filename)[0] + '.mp3'
                logger.info(f"MP3 filename: {mp3_filename}")
            return mp3_filename
        
        except yt_dlp.utils.DownloadError as e:
            logger.error(f"Download error for {video_url}: {str(e)}")
            raise Exception(f"Failed to download video: {str(e)}")
        except Exception as e:
            logger.error(f"Error converting video: {e}")
            raise e


    def convert_playlist(self, playlist_url: str) -> list:
        # Implementation for converting YouTube playlist to MP3
        pass

    def _get_base_options(self, output_path: str) -> dict:
        """Base yt-dlp options for audio extraction"""
        return {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  # 192 kbps
            }],
            'noplaylist': True,
            # Add metadata
            'writethumbnail': True,
            'embedthumbnail': True,
            # Performance options
            'concurrent_fragment_downloads': 5,
            # Quiet mode but show errors
            'quiet': True,
            'no_warnings': False,
            'logger': logger,
            'progress_hooks': [self.__my_hook],
        }

    def __my_hook(self, d):
        if d.get('status') == 'finished':
            logger.info(f"Done downloading, now converting ...")
        else:
            logger.info(f"Downloading: {d.get('_percent_str')} of {d.get('_total_bytes_str')} at {d.get('_speed_str')} ETA {d.get('_eta_str')}")

    def _check_url(self, url: str) -> bool:
        # Basic URL validation
        return "youtube.com" in url or "youtu.be" in url
        
import os
from app.utils.logger import get_logger

logger = get_logger(__name__)


def delete_file(audio_dir: str):
    """Delete all files in the specified audio directory."""

    logger.info(f"number of files before deletion: {len(os.listdir(audio_dir))}")

    if os.path.exists(audio_dir) and len(os.listdir(audio_dir)) > 0:
        for file in os.listdir(audio_dir):
            os.remove(os.path.join(audio_dir, file))
        os.rmdir(audio_dir)
    logger.info(f"All files in {audio_dir} have been deleted.")
    

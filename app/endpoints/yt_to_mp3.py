import os
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import FileResponse
from app.core.dependency import get_ytmp3_service
from app.services.base_service import IYTMP3Service
from app.utils.background_tasks import delete_file
from app.core.config import PATHS
import uuid

router = APIRouter(tags=["YouTube to MP3"])


@router.get("/yt-to-mp3")
async def yt_to_mp3(
    url: str,
    background_tasks: BackgroundTasks,
    service: IYTMP3Service = Depends(get_ytmp3_service)
                    ) -> FileResponse:
    """
    Convert a YouTube video to MP3 format.

    - **url**: The URL of the YouTube video to convert.
    """
    audio_dir = service.AUDIO_DIR
    background_tasks.add_task(delete_file, audio_dir)
    mp3_file = service.convert_video(video_url=url)
    return FileResponse(mp3_file, media_type='audio/mpeg', filename=f"{os.path.basename(mp3_file)}", background=background_tasks)
    
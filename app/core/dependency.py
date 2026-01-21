from app.services.base_service import IYTMP3Service
from app.services.yt_to_mp3_service import YTMP3Service
import uuid

def get_ytmp3_service() -> IYTMP3Service:
    request_id = str(uuid.uuid4())
    return YTMP3Service(request_id=request_id)
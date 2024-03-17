from typing import Optional
from pydantic import BaseModel


class Audio(BaseModel):
    name: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    description: str

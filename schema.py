from pydantic import BaseModel, Extra
from typing import Optional

class Urls(BaseModel, extra=Extra.ignore):
    full: str

class Image(BaseModel):
    id: Optional[str]
    width: Optional[int]=0
    height: Optional[int]=0
    description: Optional[str]=""
    urls: Urls=""


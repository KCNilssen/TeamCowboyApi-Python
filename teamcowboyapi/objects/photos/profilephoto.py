from typing import Optional
from dataclasses import dataclass

@dataclass
class Profilephoto:
    """
    object with full URLs to profile photos.
    
    Attributes:
    -----------
    fullUrl : str 
        full-size photo
    smallUrl : str 
        small size photo
    thumbUrl : str 
        thumbnail photo
    """
    fullUrl: Optional[str] = None
    smallUrl: Optional[str] = None
    thumbUrl: Optional[str] = None
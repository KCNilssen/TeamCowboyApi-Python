from typing import Union
from dataclasses import dataclass

from teamcowboyapi.objects.users import Profilephoto

@dataclass
class Postedby:
    """
    Simple object describing the user that posted the message.
    
    Attributes:
    -----------
    userId:  int 
        The user's Id
    firstName : str 
        First name of the user
    lastName : str 
        Last name of the user *
    fullName : str 
        Full name of the user *
    gender : str 
        Gender of the user (“m”, “f”, or “other”). *
    genderDisplay : str 
        Display version of the user's gender. *
    profilePhoto : object 
        Simple object with full URLs to the team's photo. *
    fullUrl : str 
        full-size photo
    thumbUrl : str 
        thumbnail photo
    """
    userId: int
    firstName: str
    lastName: str
    fullName: str
    gender: str
    genderDisplay: str
    profilePhoto: Union[Profilephoto, dict]
    fullUrl: str
    thumbUrl: str

    def __post_init__(self):
        self.profilePhoto = Profilephoto(**self.profilePhoto)
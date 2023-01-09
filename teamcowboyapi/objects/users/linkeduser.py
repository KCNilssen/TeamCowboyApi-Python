from typing import List, Union
from dataclasses import dataclass

from teamcowboyapi.objects.users import Profilephoto
from teamcowboyapi.objects.teams import Team

@dataclass
class Linkeduser:
    """
    A Team Cowboy user account that is linked to or from another Team Cowboy 
    user account.
    
    Attributes:
    -----------
    fromUserId : int
        The User Id of the “from” user in the link.
    toUserId : int
        The User Id of the “to” user in the link.
    username : str
        Username
    firstName : str
        First name
    lastName : str
        Last name
    fullName : str
        Full name
    displayName : str
        Display name
    isActive : bool
        Whether or not the link is active in the user's profile.
    profilePhoto : Profilephoto
        Simple object with full URLs to the user's profile photo.
    teams : List[Team]
        Array of simple objects representing the teams that the linked user is 
        a member of.
    """
    fromUserId: int
    toUserId: int
    username: str
    firstName: str
    lastName: str
    fullName: str
    displayName: str
    isActive: bool
    profilePhoto: Union[Profilephoto, dict]
    teams: List[Union[Team, dict]]


from typing import List, Union
from dataclasses import dataclass

from teamcowboyapi.objects.photos import Profilephoto
from teamcowboyapi.objects.teams import Teammembertype


# Begin Simpleteam

@dataclass
class Metalinkeduser:
    """
    Simple object with meta information about the user in context to the team

    Attributes:
    -----------
    teamMemberType : Teammembertype
        Information describing the user's team member type:
    options : List
        Array of options specific to the user/team pair
    """
    teamMemberType: Union[Teammembertype, dict]
    options: List

    def __post_init__(self):
        self.teamMemberType = Teammembertype(**self.teamMemberType)

@dataclass
class Simpleteam:
    """
    Simple object representing a team that the linked user is a member of
    
    Attributes:
    -----------
    teamId : int 
        Team Id
    name : str 
        The name of the team
    profilePhoto : Profilephoto
        Simple object with full URLs to the team's photo.
    meta : Metalinkeduser
        Simple object with meta information about the user in context to the 
        team.
    """
    teamId: int
    name: str
    profilePhoto: Union[Profilephoto, dict]
    meta: Union[Metalinkeduser, dict]
    
    def __post_init__(self):
        self.Profilephoto = Profilephoto(**self.Profilephoto)
        self.Metalinkeduser = Metalinkeduser(**self.Metalinkeduser)


# 
# Main Parent Object
# 

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
    teams: List[Union[Simpleteam, dict]]
    # notes: 
    # isTeamAdmin
    # invite
    # options

    def __post_init__(self):
        self.profilePhoto = Profilephoto(**self.profilePhoto)
        self.teams = Simpleteam(**self.teams)


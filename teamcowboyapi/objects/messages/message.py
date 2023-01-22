from typing import Union, List, Optional
from dataclasses import dataclass

from .postedby import Postedby
from .messagecomment import Messagecomment
from teamcowboyapi.objects.users import Usermetainfo

# Begin Simplemessageteam

@dataclass
class Simplemessageteam:
    """
    Simple object describing the team that the message is assigned to.
    
    Attributes:
    -----------
    teamId : int 
        The team Id
    name : str 
        The team name
    """
    teamId: int
    name: str



# 
# Main Parent Object
# 

@dataclass
class Message:
    """
    A message for a team's message board.

    Attributes
    ----------
    messageId : int
        The message Id.
    title : str
        The title of the message.
    bodyHtml : str
        The body of the message (HTML).
    bodyText : str
        A text approximation of the HTML message. Note that messages are 
        natively stored as HTML, so the text version provided in this property 
        may not be perfect or as the author intended it. In some cases, it may 
        be preferred to convert HTML to text using your own code libraries in 
        your applications.
    isPinned : bool
        True if the message is a “pinned” message (pinned messages always show 
        at the top of the message list on the main Team Cowboy web site).
    allowComments : bool
        True if comments can be posted for the message.
    commentCount : int  
        The number of comments that have been posted for the message.
    team : Union[Messageteam, dict]
        Simple object describing the team that the message is assigned to.
    postedBy : Union[Postedby, dict]
        Simple object describing the user that posted the message.
        * Due to user privacy settings, the last name, profile photo URL(s), 
        and/or gender values may not be present. This also affects the display 
        of the full name if no last name is available (the full name will be 
        the same as the first name).
    comments : List[Union[Messagecomment, dict]]
        Array of MessageComment objects. Only present if comments are loaded 
        for the message.
    userMetaInfo : Union[Usermetainfo, dict]
        Simple object representing meta information about the API user in 
        context of the team that the message applies to.
    dateCreatedLocal : str #date/time
        Date/time the message was created (local time for the message's team).
    dateLastUpdatedLoca l: str #date/time
        Date/time the message was last updated (local time for the message's 
        team).
    dateCreatedUtc : str #date/time
        Date/time the message was created (UTC).
    dateLastUpdatedUtc : str #date/time
        Date/time the message was last updated (UTC).
    """
    messageId: int
    title: str
    bodyHtml: str
    bodyText: str
    isPinned: bool
    allowComments: bool
    commentCount: int
    team: Union[Simplemessageteam, dict]
    postedBy: Union[Postedby, dict]
    userMetaInfo: Union[Usermetainfo, dict]
    dateCreatedLocal: str #date/time
    dateLastUpdatedLocal: str #date/time
    dateCreatedUtc: str #date/time
    dateLastUpdatedUtc: str #date/time
    comments: Optional[List[Union[Messagecomment, dict]]] = None

    def __post_init__(self):
        self.team = Simplemessageteam(**self.team)
        self.postedBy = Postedby(**self.postedBy)
        self.userMetaInfo = Usermetainfo(**self.userMetaInfo)
        self.comments = Messagecomment(**self.comments) if self.comments else None
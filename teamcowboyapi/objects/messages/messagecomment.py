from typing import Union
from dataclasses import dataclass

from .postedby import Postedby

@dataclass
class Messagecomment:
    """
    A comment for a post on a team’s message board.
    
    Attributes:
    -----------
    commentId : int
        The message comment Id.
    messageId : int
        The Id of the message that the comment is associated with.
    teamId : int
        The Id of the team that the message is associated with.
    timezoneId : str
        The timezone Id for the comment (pulled from the team's timezone).
    postedBy : Union[Postedby, dict]
        Simple object describing the user that posted the message comment.
        * Due to user privacy settings, the last name, profile photo URL(s), 
        and/or gender values may not be present. This also affects the display 
        of the full name if no last name is available (the full name will be 
        the same as the first name).
    dateCreatedLocal : str
        Date/time the comment was posted (local time for the message's team).
    dateLastUpdatedLocal : str
        Date/time the comment was posted (local time for the message's team).
    dateCreatedUtc : str
        Date/time the comment was posted (UTC).
    dateLastUpdatedUtc : str
        Date/time the comment was last posted(UTC).
    """
    commentId: int
    messageId: int
    teamId: int
    timezoneId: str
    postedBy: Union[Postedby, dict]
    dateCreatedLocal: str
    dateLastUpdatedLocal: str
    dateCreatedUtc: str
    dateLastUpdatedUtc: str

    def __post_init__(self):
        self.postedBy = Postedby(**self.postedBy)
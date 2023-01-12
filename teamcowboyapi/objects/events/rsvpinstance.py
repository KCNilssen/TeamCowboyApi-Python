from typing import Union, List
from dataclasses import dataclass

from teamcowboyapi.objects.teams import Teammembertype

# Begin Allowedstatusesdisplay

@dataclass
class Allowedstatusesdisplay:
    """
    Simple objects for allowed statuses displayed

    Attributes:
    -----------
    status : str
        Status name (corresponding with the value in the allowedStatuses 
        property)
    statusDisplay : str
        Display value for the status in context of the event (takes event 
        type, past/future event, and other information into consideration)
    """
    status: str
    statusDisplay: str


# Begin Rsvpdetails

@dataclass
class Rsvpdetails:
    """
    Simple object describing RSVP information and other details for the 
    current RSVP instance (e.g., the current user or another user they can 
    RSVP on behalf of).
    
    Attributes:
    -----------
    allowRSVP : bool 
        Whether or not the user/instance is allowed to RSVP
    allowRsvpRemoval : bool  
        Whether or not the user/instance is allowed to remove their RSVP once 
        it has been submitted
    allowExtraPlayers : bool) 
        Whether or not the user/instance is allowed to include additional team 
        members in their RSVP
    allowedStatuses : List[str] 
        Array of strings representing the RSVP statuses that the user/instance 
        is allowed to submit. Value will be “yes”, “maybe”, “available”, or 
        “no”.
    allowedStatusesDisplay : List[Allowedstatusesdisplay] 
        Array of simple objects:
    status : str 
        the current RSVP status for the user/instance. Value will be “yes”, 
        “maybe”, “available”, “no”, or “noresponse”.
    statusDisplay : str 
        The user-facing RSVP status for the user/instance. This will vary 
        based on the event type. For example, for a “Game” event type, a 
        “yes” RSVP will be displayed as “Playing”.
    statusDisplayShort : str 
        A shorter version of the user-facing RSVP display value. This will 
        often be the same as the “long” version, but not always.
    addlMale : int 
        The number of additional male team members on the RSVP for the 
        user/instance
    addlMaleDisplay : str 
        The display value for the addlMale property. This will generally be 
        the same if a value is present for addlMale, or will be blank if no 
        additional male team members are present.
    addlFemale : int 
        The number of additional female team members on the RSVP for the 
        user/instance
    addlFemaleDisplay : str 
        The display value for the addlFemale property. This will generally be 
        the same if a value is present for addlFemale, or will be blank if no 
        additional female team members are present.
    comments : str 
        RSVP comments provided for the user/instance
    """
    allowRSVP: bool
    allowRsvpRemoval: bool
    allowExtraPlayers: bool
    allowedStatuses: List[str]
    allowedStatusesDisplay: List[Union[Allowedstatusesdisplay, dict]]
    status: str
    statusDisplay: str
    statusDisplayShort: str
    addlMale: int
    addlMaleDisplay: str
    addlFemale: int
    addlFemaleDisplay: str
    comments: str

    def __post_init__(self):
        self.allowedStatusesDisplay = [Allowedstatusesdisplay(**asd) for asd in self.allowedStatusesDisplay]


# 
# Main Parent Object
# 

@dataclass
class Rsvpinstance:
    """
    Information for an “RSVP instance” which is a representation of RSVP 
    display values, rules, and other information that can be used to build 
    user interface input controls for collecting a user's RSVP for an event. 
    An RSVP instance can be for the current user or it can be for one of the 
    current users' linked users.

    Attributes:
    -----------
    userId : int
        Id of the user that the RSVP instance applies to.
    displayName : str
        Display string to use in the user interface. This is mean to be read 
        from the current user's point of view, so if the userId for the RSP 
        instance is the current user, this will be something like, 
        “Your status” whereas for any of the current user's linked users, it 
        will be the display name of the linked user.
    teamMemberType : Teammembertype
        A TeamMemberType object for the user that the RSVP instance applies to.
    rsvpDetails : Rsvpdetails
        Simple object describing RSVP information and other details for the 
        current RSVP instance (e.g., the current user or another user they can 
        RSVP on behalf of).
    """ 
    userId: int
    displayName: str
    teamMemberType: Union[Teammembertype, dict]
    rsvpDetails: Union[Rsvpdetails, dict]

    def __post_init__(self):
        self.teamMemberType = Teammembertype(**self.teamMemberType)
        self.rsvpDetails = Rsvpdetails(**self.rsvpDetails)
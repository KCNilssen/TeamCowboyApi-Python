from typing import List, Union, Optional
from dataclasses import dataclass

from teamcowboyapi.objects.users import Linkeduser
from teamcowboyapi.objects.photos import Profilephoto
from teamcowboyapi.objects.teams import Teammembertype

@dataclass
class Invite:
    """
    information describing the invitation status for the user:

    Attributes:
    -----------    
    status : str
        invitation status (accepted, rejected, pending)
    guid : str
        unique invitation GUID
    dateSentLocal : str
        Date/time the invite was sent (in the team's timezone)
    dateLastUpdatedLocal : str
        Date/time the invite was last updated (in the team's timezone)
    dateSentUtc : str
        Date/time the invite was sent (UTC)
    dateLastUpdatedUtc : str
        Date/time the invite was last updated (UTC)

    """
    status: str
    guid: str
    dateSentLocal: str 
    dateLastUpdatedLocal: str 
    dateSentUtc: str 
    dateLastUpdatedUtc: str 

@dataclass
class Teammeta:
    """
    Simple object describing team-specific information. This property is only 
    present if the User is being returned in context to a team or event 
    attendance list.
    NOTE:  If reading user information from a call to the event attendance 
    list (e.g., Event_GetAttendanceList), only the teamMemberType property 
    will be populated below. All other values will not be present.

    Attributes:
    -----------
    teamMemberType : Teammembertype
        A team member type that is assigned to a team member (or is available 
        to be assigned to a team member).
    notes : str 
        Admin-only notes for the team member
    isTeamAdmin : bool 
        Whether or not the user is an admin on the team
    invite : Invite 
        information describing the invitation status for the user:
    options : list  
        Array of options specific to the user on the team
    """
    teamMemberType: Union[Teammembertype, dict]
    notes: Optional[str] = None
    isTeamAdmin: Optional[bool] = None
    invite: Optional[Union[Invite, dict]] = None
    options: Optional[list] = list 

    def __post_init__(self):
        self.teamMemberType = Teammembertype(**self.teamMemberType)
        self.invite = Invite(**self.invite) if self.invite else None

@dataclass
class Linkedusers:
    """
    Simple object describing users that are linked to and/or from the user. 
    Object will be empty if the user has no linked users. This property is not 
    present if the User is being returned in context to a team.

    Attributes:
    -----------
    linkedTo : List[Linkeduser]
        An array of LinkedUser objects representing the users that the user is linked to
    linkedBy : List[Linkeduser] 
        An array of LinkedUser objects representing the users that are linked to the user
    """
    linkedTo: List[Union[Linkeduser, dict]]
    linkedBy: List[Union[Linkeduser, dict]] 

    def __post_init__(self):
        self.linkedTo = [Linkeduser(**link) for link in self.linkedTo]
        self.linkedBy = [Linkeduser(**link) for link in self.linkedBy]

@dataclass
class User:
    """
    A user in the Team Cowboy system. Users may be on one or more teams (or no 
    teams at all).

    IMPORTANT NOTE:  User profile information can be overridden for specific 
    teams that the user is a member of. Because of this, profile information 
    returned in a User object will either be for the core user profile or it 
    will be for the user in context to a specific team. This is based on the 
    API method that was called. For example, the User object returned from the 
    User_Get method call will be in context of the user themselves whereas the 
    array of User objects returned from a Team_GetRoster method call will be 
    in context of the team passed with the method call via the teamId parameter.
 
    Also note that some method calls that return User objects may return an 
    abridged version of the object which has fewer properties populated. For 
    example, Event_GetAttendanceList returns an AttendanceList object which 
    includes and object that has a User object as its property. This User 
    object does not include all of the properties listed below (such as 
    detailed contact information and profile information) because that 
    information is not relevant to displaying the attendance list.
    
    Attributes:
    -----------
    userId : int
        User Id
    firstName : str
        First name
    lastName : str
        Last name
    fullName : str
        Full name (first and last names combined)
    displayName : str
        Display name
    emailAddress1 : str
        E-mail address 1
    emailAddress2 : str
        E-mail address 2
    phone1 : str    
        Phone number 1
    phone2 : str
        Phone number 2
    gender : str
        Gender
        Possible values:
            m - Male
            f - Female
            other - Other/Not specified
    genderDisplay : str
        Gender display value
    birthDate_month : int
        Birthdate month (01 through 12)
    birthDate_day : int
        Birthdate day (01 through 31)
    birthDate_year : int
        Birthdate year (4-digit year)
    shirtNumber : str
        Shirt number
    shirtSize : str
        Shirt size (may be a numeric size or a standard size like S, M, L, etc.)
    pantsSize : str
        Pants size (may be a numeric size or a standard size like S, M, L, etc.)
    options : list #!
        An array of options that pertain to the user.
        NOTE: This property is only populated for the user that is associated 
        with the user token passed in the API call (i.e., only the current 
        user's options are populated).
    profilePhoto : Profilephoto
        Simple object with full URLs to the user's profile photo.
    teamMeta : Teammeta #!?
        Simple object describing team-specific information. This property is 
        only present if the User is being returned in context to a team or 
        event attendance list.
        NOTE:  If reading user information from a call to the event attendance 
        list (e.g., Event_GetAttendanceList), only the teamMemberType property 
        will be populated below. All other values will not be present.
    linkedUsers : Linkedusers
        Simple object describing users that are linked to and/or from the 
        user. Object will be empty if the user has no linked users. This 
        property is not present if the User is being returned in context to a 
        team.
    dateCreatedUtc : str
        Date/time the user was created (UTC). This property is not present if 
        the User is being returned in context to a team.
    dateLastUpdatedUtc : str
        Date/time the user was last updated (UTC).
    dateLastSignInUtc : str
        Date/time the user last signed in (UTC).
    """
    userId: int
    firstName: str
    lastName: str
    fullName: str
    displayName: str
    emailAddress1: str
    emailAddress2: str
    phone1: str
    phone2: str
    gender: str
    genderDisplay: str
    profilePhoto: Union[Profilephoto, dict]
    dateCreatedUtc: str
    dateLastUpdatedUtc: str
    dateLastSignInUtc: str
    teamMeta: Optional[Union[Teammeta, dict]] = None
    shirtNumber: Optional[str] = None
    shirtSize: Optional[str] = None
    pantsSize: Optional[str] = None
    options: Optional[list] = None
    linkedUsers: Optional[Union[Linkedusers, dict]] = None
    birthDate_month: Optional[int] = None
    birthDate_day: Optional[int] = None
    birthDate_year: Optional[int] = None

    def __post_init__(self):
        self.profilePhoto = Profilephoto(**self.profilePhoto)
        self.linkedUsers = Linkedusers(**self.linkedUsers) if self.linkedUsers else None
        self.teamMeta = Teammeta(**self.teamMeta) if self.teamMeta else None


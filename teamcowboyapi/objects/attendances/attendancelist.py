from typing import Union, List
from dataclasses import dataclass

from teamcowboyapi.objects.teams import Teammembertype
from teamcowboyapi.objects.users import User



# 
# Begin Attendancecount
# 

@dataclass
class Count:
    """
    Object containing counts:

    Attributes:
    -----------
    byGender : dict
        Counts by gender
    byType : dict  
        Counts by type
    total : int
        Total counts
    """
    byGender: dict
    byType: dict
    total: int

@dataclass
class Attendancecount:
    """
    An array of simple objects, each describing attendance count information 
    by RSVP status.

    Attributes:
    -----------
    status : str
        The RSVP status name
    counts : Count
         Object containing counts
    """
    status: str 
    counts: Union[Count , dict]

    def __post_init__(self):
        self.counts = Count(**self.counts)


# 
# Begin Metaattendancelist
# 

@dataclass
class Gender:
    """
    Simple object describing a gender:

    Attribtutes:
    ------------
    gender : str  
        Gender name
    genderDisplay : str 
        Gender display value/title
    """
    gender: str
    genderDisplay: str

@dataclass
class Rsvpstatuse:
    """
    Object describing a RSVP:

    Attributes:
    -----------
    status : str

    statusDisplay : str

    """
    status: str
    statusDisplay: str

@dataclass
class Miscmeta:
    """
    object with miscellaneous values:

    Attributes:
    -----------
    genderLabel_male : str 
        display label to use for male gender, as defined by the team.
    genderLabel_female : str 
        display label to use for male gender, as defined by the team.
    genderLabel_other : str 
        display label to use for male gender, as defined by the team.
    groupBy : str 
        preferred secondary grouping of team members in the Attendance List 
        (after grouping by RSVP status). Possible values:  none 
        (no sub-grouping), teamMemberType (group by team member type), gender 
        (group by gender)
    """
    genderLabel_male: str
    genderLabel_female: str
    genderLabel_other: str
    groupBy: str

@dataclass
class Metaattendancelist:
    """
    Object that contains meta information for looping through and displaying 
    attendance list information.

    Attributes:
    -----------
    teamMemberTypes : List[Teammembertype] 
        array of TeamMemberType objects.
    genders : List[Gender] 
        array containing simple objects describing the genders:
    rsvpStatuses : List[Rsvpstatuse] 
        array of objects describing the RSVP statuses:
    misc : Miscmeta 
        object with miscellaneous values:
    """
    teamMemberTypes: List[Union[Teammembertype, dict]] 
    genders: List[Union[Gender, dict]] 
    rsvpStatuses: List[Union[Rsvpstatuse, dict]] 
    misc: Union[Miscmeta, dict]

    def __post_init__(self):
        self.teamMemberTypes = [Teammembertype(**membertype) for membertype in self.teamMemberTypes]
        self.genders = [Gender(**gender) for gender in self.genders]
        self.rsvpStatuses = [Rsvpstatuse(**rsvpstatuse) for rsvpstatuse in self.rsvpStatuses]
        self.misc = Miscmeta(**self.misc)


# 
# Begin Rsvpid
# 

@dataclass
class Bygender:
    """
    Object with properties listing userIds:

    Attributes:
    -----------
    m : List[int]
        array of user Ids
    f : List[int]
        array of user Ids
    """
    m: List[int]
    f: List[int]

@dataclass
class Bytype:
    """
    Object with properties listing userIds:

    Attributes:
    -----------
    typeName1 : List[int] 
        array of user Ids
    typeName2 : List[int] 
        array of user Ids
    typeNameN : List[int] 
        array of user Ids
    """
    typeName1: List[int]
    typeName2: List[int]
    typeNameN: List[int]

@dataclass
class Userid:
    """"
    Object with properties listing userIds:
    Refer to the meta property for a list of RSVP statuses.

    Attributes:
    -----------
    byGender : Bygender

    byType : Bytype

    all : List[int]
        array of user Ids
    """
    byGender: Union[Bygender, dict]
    byType: Union[Bytype, dict]
    all: List[int]

@dataclass
class Rsvpid:
    """
    Object that provides user ID by RSVP status.

    Attributes:
    -----------
    status : str 
        RSVP status name
    userIds : Userid 
        object with properties listing userIds
    """
    status: str 
    userIds: Union[Userid, dict]

    def __post_init__(self):
        self.userIds = Userid(**self.userIds)


# 
# Begin Usersattendancelist
# 

@dataclass
class Attendancelistuserinfo:
    """
    Attendance list/RSVP information for a given user in context of an event.
    
    Attributes:
    -----------
    status : str
        RSVP status
    statusDisplay : str
        RSVP status display value
    comments : str
        Comments
    canRSVP : bool
        True if the user can RSVP for the event based on the event, team 
        member, and team settings.
    hasResponded : bool
        True if an RSVP response has been recorded for the user (i.e., if the 
        user has not yet responded for the event, this will be false).
    addlMale : int
        The number of additional male attendees that are a “yes” RSVP that 
        this team member has included with their RSVP.
    addlFemale : int
        Same as addlMale, but for females.
    addlDisplay : str
        A string describing the additional male and/or female players.
    dateCreatedLocal : str
        The date/time when the RSVP was first saved, in the event's timezone.
    dateLastUpdatedLocal : str
        The date/time when the RSVP was last updated, in the event's timezone.
    dateCreatedUtc : str
        The date/time when the RSVP was first saved (UTC).
    dateLastUpdatedUtc : str
        The date/time when the RSVP was last updated (UTC).
    """
    status: str
    statusDisplay: str
    comments: str
    canRSVP: bool
    hasResponded: bool
    addlMale: int
    addlFemale: int
    addlDisplay: str
    dateCreatedLocal: str
    dateLastUpdatedLocal: str
    dateCreatedUtc: str
    dateLastUpdatedUtc: str

@dataclass
class Usersattendancelist:
    """

    Attributes:
    -----------
    user: User 
        An abridged version of the User object.
    rsvpInfo: Attendancelistuserinfo 
        AttendanceListUserInfo object.
    """
    user: Union[User, dict]
    rsvpInfo: Union[Attendancelistuserinfo, dict]

    def __post_init__(self):
        self.user = User(**self.user)
        self.rsvpInfo = Attendancelistuserinfo(**self.rsvpInfo)



# 
# Main Parent Object
# 

@dataclass
class Attendancelist:
    """
    Attendance list information for a given event.

    Attributes:
    -----------
    countsByStatus : List[Attendancecount]
        An array of simple objects, each describing attendance count 
        information by RSVP status.
        Refer to the meta property of the AttendanceList object for a list of 
        RSVP statuses.
    meta : Metaattendancelist
        Object that contains meta information for looping through and 
        displaying attendance list information.
    usersIdsByStatus : List[Rsvpid]
        An array of simple objects that provides user IDs by RSVP status.
        Refer to the meta property for a list of RSVP statuses.
    users : List[Usersattendancelist]
        An array of users for the attendance list. Each array element is an 
        object describing the user as well as attendance list information for 
        the user in context of the event.
    """
    countsByStatus: List[Union[Attendancecount, dict]]
    meta: Metaattendancelist
    userIdsByStatus: List[Union[Rsvpid, dict]]
    users: List[Union[Usersattendancelist, dict]]

    def __post_init__(self):
        self.countsByStatus = [Attendancecount(**status) for status in self.countsByStatus]
        self.meta = Metaattendancelist(**self.meta)
        self.userIdsByStatus = [Rsvpid(**status) for status in self.userIdsByStatus]
        self.users = [Usersattendancelist(**user) for user in self.users]
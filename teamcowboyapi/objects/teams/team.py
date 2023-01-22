from typing import Optional, Union
from dataclasses import dataclass

from teamcowboyapi.objects.activitys import Activity
from teamcowboyapi.objects.photos import Profilephoto
from teamcowboyapi.objects.colorswatches import Colorswatch

from .teammembertype import Teammembertype

# Begin Teamtype

@dataclass
class Teamtype:
    """
    Team type (adult, youth, etc.).

    Attributes
    ----------
    name : str
        Type name
    title : str
        Title/display name.
    """
    name: str
    title: str
    

# Begin Simpleteammember

@dataclass
class Simpleteammember:
    """
    Simple object describing the team member that is assigned

    Attributes
    ----------
    userId : int
        User Id
    firstName : str
        First name
    lastName : str
        Last name
    fullName : str
        Full name (first and last names combined)
    emailAddress : str
        E-mail address
    """
    userId: int
    firstName: str
    lastName: str
    fullName: str
    emailAddress: str


# Begin Teamcolorswatches

@dataclass
class Teamcolorswatches:
    """
    Simple object describing 0 or more color swatches for the team.

    Attributes
    ----------
    home : Colorswatch 
        “Home” color swatch for the team
    away : Colorswatch 
        “Away” color swatch for the team
    alternate : Colorswatch 
        “Alternate” color swatch for the team
    """
    home: Optional[Colorswatch] = None
    away: Optional[Colorswatch] = None
    alternate: Optional[Colorswatch] = None 

    def __post_init__(self):
        self.home = Colorswatch(**self.home) if self.home else None
        self.away = Colorswatch(**self.away) if self.away else None
        self.alternate = Colorswatch(**self.alternate) if self.alternate else None


# Begin Teamoptions

@dataclass
class Miscoptions:
    """
    Simple object:

    Attributes
    ----------
    showRecord : bool 
        Whether or not to show record (wins/losses/ties) for event schedules.
    attendanceListMaleLabel : str 
        The label to use for male team members on the team
    attendanceListFemaleLabel : str 
        The label to use for female team members on the team
    hideGenders : bool 
        Whether or not to hide the display of genders for the team
    """
    showRecord: bool
    attendanceListSeparateGenders: bool
    attendanceListMaleLabel: str
    attendanceListFemaleLabel: str
    attendanceListOtherGenderLabel: str
    hideGenders: bool

@dataclass
class Teamoptions:
    """
    Simple object with a subset of team options.

    Attributes
    ----------
    misc : Miscoptions
        Simple object
    """
    misc: Miscoptions

    def __post_init__(self):
        self.misc = Miscoptions(**self.misc)


# Begin Simpleteamuserprofile

@dataclass
class Simpleteamuserprofile:
    """
    Simple object with profile information for the user that is specific to 
    the team (i.e., information that may be overridden from the user’s core 
    profile information).

    NOTE: This information will only be present in the team object if the 
    team was being loaded from a User method (such as User_GetTeams).
    
    Attributes
    ----------
    firstName : str 
        First name
    lastName : str 
        Last name
    fullName : str 
        Full name (first and last name combined)
    displayName : str 
        Display name
    emailAddress : str 
        E-mail address 1
    emailAddress2 : str 
        E-mail address 2
    phone1 : str 
        Phone number 1
    phone2 : str 
        Phone number 2
    gender : str 
        Gender
    genderDisplay : str 
        Gender display value
    shirtNumber : str 
        Shirt number
    shirtSize : str 
        Shirt size
    pantsSize : str 
        Pants size
    profilePhoto : object
        Profile photo
    options : list
        Array of options specific to the user/team pair
    isTeamAdmin : bool
        Whether or not the user is an administrator on the team
    birthDate_month : int
        birthday month`
    birthDate_day : int
        birthday day
    birthDate_year : int
        birthday year
    """
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
    shirtNumber: str
    shirtSize: str
    pantsSize: str
    profilePhoto: Union[Profilephoto, dict]
    options: list
    isTeamAdmin: bool
    birthDate_month: Optional[int] = None
    birthDate_day: Optional[int] = None
    birthDate_year: Optional[int] = None

    def __post_init__(self):
        self.profilePhoto = Profilephoto(**self.profilePhoto)


# Begin Teammeta

@dataclass
class Teammeta:
    """
    Simple object with meta information about the user in context to the team.
 
    NOTE: This information will only be present in the team object if the team 
    was being loaded from a User method (such as User_GetTeams).

    Attributes:
    -----------
    teamMemberType : object
        TeamMemberType
    isHiddenByUser : bool
        true if the user has hidden the team from their profile
    showOnDashboard : bool
        true if the user is showing the team on their dashboard
    """
    teamMemberType: Union[Teammembertype, dict]
    isHiddenByUser: bool
    showOnDashboard: bool

    def __post_init__(self):
        self.teamMemberType = Teammembertype(**self.teamMemberType)


# 
# Main Parent Object
# 

@dataclass
class Team:
    """
    A team on the Team Cowboy web site.

    Attributes
    ----------
    teamId : int
        Team Id
    name : str
        Team name
    shortName : str
        Short team name. Will be truncated version of name if the value of 
        name is long.
    type : Union[Teamtype, dict]
        Team type (adult, youth, etc.).
    activity : Union[Activity, dict]
        An activity/sport that is typically associated with teams or team 
        seasons.
    timezoneId : str
        Timezone Id where the team is located.
    city : str
        City where the team is located
    stateProvince : str
        State/province where the team is located.
    stateProvinceAbbrev : str
        State/province abbreviation (e.g., “WA” for “Washington” or “ON” 
        for “Ontario”).
    country : str
        Country where the team is located.
    countryIso3 : str
        SO3 value for the team's country (e.g., “USA” for “United States of 
        America”). See http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
    postalCode : str
        Zip/Postal code where the team is located.
    locationDisplayShort : str
        String that can be used to output the team's location, which includes 
        the state/province, city, and country. The “short” version uses the 
        state/province abbreviation and ISO3 value for the country.
    locationDisplayLong : str
        Same as locationDisplayShort, except uses full values for the 
        state/province and country (instead of using abbreviation and ISO3 
        country code).
    teamPhoto : Union[Teamphoto, dict]
        Simple object with full URLs to the current team photo. Only 
        returned if team has a photo.
    colorSwatches : Colorswatches
        Simple object describing 0 or more color swatches for the team.
        Properties will be null if no color swatch is defined for the team.
    options : Options
        Simple object with a subset of team options.
    userProfileInfo : Userprofileinfo
        Simple object with profile information for the user that is specific 
        to the team (i.e., information that may be overridden from the user's 
        core profile information).
        NOTE: This information will only be present in the team object if the 
        team was being loaded from a User method (such as User_GetTeams).
    meta : Meta
        Simple object with meta information about the user in context to the 
        team.
        NOTE: This information will only be present in the team object if the 
        team was being loaded from a User method (such as User_GetTeams).
    dateCreatedUtc : str #date/time
        Date/time the team was created (UTC).
    dateLastUpdatedUtc : str #date/time
        Date/time the team was last updated (UTC).
    managerUser : Optional[Simpleteammember] = None
        Simple object describing the team member that is assigned as the 
        manager for the team. Note that this team member may not necessarily 
        have team administration privileges (the manager is for display 
        purposes only). Also note that some fields below may not be populated 
        based on permission and user privacy settings for the user accessing 
        the API.
        The value of this property will be NULL if no manager is defined for 
        the team.
    captainUser : Optional[Simpleteammember] = None
        Simple object describing the team member that is assigned as the 
        captain for the team.
        See description and object properties for managerUser.
    """
    teamId: int
    name: str
    shortName: str
    type: Union[Teamtype, dict]
    activity: Union[Activity, dict]
    timezoneId: str
    city: str
    stateProvince: str
    stateProvinceAbbrev: str
    country: str
    countryIso3: str
    postalCode: str
    locationDisplayShort: str
    locationDisplayLong: str
    colorSwatches: Union[Teamcolorswatches, dict] # Property will be null if no color swatch is defined
    options: Union[Teamoptions, dict]
    dateCreatedUtc: str #date/time
    dateLastUpdatedUtc: str #date/time
    userProfileInfo: Optional[Union[Simpleteamuserprofile, dict]] = None
    meta: Optional[Union[Teammeta, dict]] = None
    teamPhoto: Optional[Union[Profilephoto, dict]] = None
    managerUser: Optional[Simpleteammember] = None
    captainUser: Optional[Simpleteammember] = None

    def __post_init__(self):
        self.type = Teamtype(**self.type)
        self.activity = Activity(**self.activity)
        self.colorSwatches = Teamcolorswatches(**self.colorSwatches)
        self.options = Teamoptions(**self.options)
        self.userProfileInfo = Simpleteamuserprofile(**self.userProfileInfo) if self.userProfileInfo else None
        self.meta = Teammeta(**self.meta) if self.meta else None
        self.teamPhoto = Profilephoto(**self.teamPhoto) if self.teamPhoto else None
        self.managerUser = Simpleteammember(**self.managerUser) if self.managerUser else None
        self.captainUser = Simpleteammember(**self.captainUser) if self.captainUser else None
from typing import Union, Optional, List
from dataclasses import dataclass

from .rsvpinstance import Rsvpinstance
from teamcowboyapi.objects.locations import Location
from teamcowboyapi.objects.colorswatches import Colorswatch
from teamcowboyapi.objects.users import Usermetainfo

# Begin Simpleteam

@dataclass
class Simpleteam:
    """
    Simple object with basic team information.

    Attributes
    ----------
    teamId : int
        Team Id
    name : str
        Team name
    """
    teamId: int
    name: str


# Begin Eventresult

@dataclass
class Eventresult:
    """
    Simple object describing the outcome/result of the event.

    Attributes:
    -----------
    scoreEntered : bool
        True if a score has been entered for the event
    outcome : str
        outcome for the event: win, loss, tie, NULL
    score1 : int
        Score entered for the main team
    score2 : int
        Score entered for the opponent team
    isWin : bool
        True if the event was a win
    isTie : bool
        True if the event was a tie
    isLoss : bool
        True if the event was a loss
    scoreDisplay : str
        Display of the outcome and the scores
    dhScoreEntered : bool
        Same as scoreEntered, but for the 2nd game in a doubleheader event
    dhOutcome : str
        Same as outcome, but for the 2nd event in a doubleheader event
    dhScore1 : int
        Same as score1, but for the 2nd game in a doubleheader event
    dhScore2 : int
        Same as score2, but for the 2nd game in a doubleheader event
    dhIsWin : bool
        Same as isWin, but for the 2nd game in a doubleheader event
    dhIsTie : bool
        Same as isTie, but for the 2nd game in a doubleheader event
    dhIsLoss : bool
        Same as isLoss, but for the 2nd game in a doubleheader event
    dhScoreDisplay : str
        Same as scoreDisplay, but for the 2nd game in a doubleheader event
    """ 
    scoreEntered: bool
    outcome: str
    score1: int
    score2: int
    isWin: bool
    isTie: bool
    isLoss: bool
    scoreDisplay: str
    dhScoreEntered: bool
    dhOutcome: str
    dhScore1: int
    dhScore2: int
    dhIsWin: bool
    dhIsTie: bool
    dhIsLoss: bool
    dhScoreDisplay: str


# Begin Datetimeinfo

@dataclass
class Datetimeinfo:
    """
    Simple object describing date/time information for the event.

    Attributes:
    -----------
    timezoneId : str 
        Timezone Id for the event
    startDateLocal : str 
        The start date of the event in the event's timezone in the format YYYY-MM-DD
    startTimeLocal : str 
        The start time of the event in the event's timezone, in the format HH:MM:SS
    startDateTimeLocal : str T
        he combined start date and time for the event in the event's timezone, in the format YYYY-MM-DD HH:MM:SS
    startDateLocalDisplay : str 
        The display version of the start date of the event in the event's timezone
    startTimeLocalDisplay : str 
        The display version of the start time of the event in the event's timezone
    startDateTimeLocalDisplay : str 
        The display version of the combined start date and time of the event in the event's timezone
    startDateTimeUtc : str 
        The start date/time of the event in UTC, in the format YYYY-MM-DD HH:MM:SS
    startTimeTBD : bool 
        True if the start time is marked as “TBD”. Note that this is not the same as an event without a time. This indicates the event explicitly has the “Time TBD” flag set.
    endDateLocal : str 
        The end date of the event in the event's timezone in the format YYYY-MM-DD
    endTimeLocal : str 
        The end time of the event in the event's timezone, in the format HH:MM:SS
    endDateTimeLocal : str 
        The combined end date and time for the event in the event's timezone, in the format YYYY-MM-DD HH:MM:SS
    endDateLocalDisplay : str 
        The display version of the end date of the event in the event's timezone
    endTimeLocalDisplay : str 
        The display version of the end time of the event in the event's timezone
    endDateTimeLocalDisplay : str 
        The display version of the combined end date and time of the event in the event's timezone
    endDateTimeUtc : str 
        The end date/time of the event in UTC, in the format YYYY-MM-DD HH:MM:SS
    endTimeTBD : bool 
        True if the end time is marked as “TBD”. Note that this is not the same as an event without a time. This indicates the event explicitly has the “Time TBD” flag set.
    inPast : bool 
        True if the event is in the past
    inFuture : bool 
        True if the event is in the future
    """ 
    timezoneId: str
    startDateLocal: str
    startTimeLocal: str
    startDateTimeLocal: str
    startDateLocalDisplay: str
    startTimeLocalDisplay: str
    startDateTimeLocalDisplay: str
    startDateTimeUtc: str
    startTimeTBD: bool
    endDateLocal: str
    endTimeLocal: str
    endDateTimeLocal: str
    endDateLocalDisplay: str
    endTimeLocalDisplay: str
    endDateTimeLocalDisplay: str
    endDateTimeUtc: str
    endTimeTBD: bool
    inPast: bool
    inFuture: bool


# Begin Shirtcolors

@dataclass
class Shirtcolors:
    """
    Simple object representing the team shirt colors.

    Attributes:
    -----------
    team1 : ColorSwatch 
        ColorSwatch object describing the color swatch for the main team (the 
        team the event is assigned to). Value is null if no color swatch is 
        present.
    team2 : ColorSwatch 
        ColorSwatch object describing the color swatch for the opponent/other 
        team. Value is null if no color swatch is present.
    """ 
    team1: Optional[Union[Colorswatch, dict]] = None
    team2: Optional[Union[Colorswatch, dict]] = None

    def __post_init__(self):
        self.team1 = Colorswatch(**self.team1) if self.team1 else None
        self.team2 = Colorswatch(**self.team2) if self.team2 else None



# 
# Main Parent Object
# 

@dataclass
class Event:
    """
    An event in a team's event schedule.
    
    Attributes:
    -----------
    eventId : int
        Event Id
    team : Eventteam
        Simple object with basic team information.
    seasonId : int
        Season Id
    seasonName : str
        Season name
    eventType : str
        Event type enumeration.
        Possible values:  game, doubleheader, postseason, match, meet, 
        tournament, jamboree, race, regatta, ride, bye, practice, scrimmage, 
        pickup, meeting, other
    eventTypeDisplay : str
        Event type display
    status : str
        Event status enumeration.
        Possible values:  active, postponed, canceled, forfeited
    statusDisplay : str
        Event status display
    personNounSingular : str
        Team member noun display (singular). E.g., player, competitor, 
        attendee, etc.
    personNounPlural : str
        Team member noun display (plural). E.g., players, competitors, 
        attendees, etc.
    title : str
        Title of the event. This varies based on the event type. For 
        game-related events (game, meet, race, etc), this is the opponent 
        name. For other events types, this is the event title.
    titleFull : str
        The full title of the event. This takes into consideration opponent 
        names (for events where that is applicable), etc. For game-related 
        events (game, meet, race, etc), this would be something like “Home vs. 
        OpponentName”. For other events types, this is the event title or 
        just the user-facing version of the event type (such as “Practice”).
    titleLabel : str
        The label to use for the event title. Like the title value itself, this 
        varies based on the event type.
    homeAway : str
        Whether the event is home or away (enumeration).
        Possible values:  home, away, NULL
    result : Eventresult
        Simple object describing the outcome/result of the event.
    rsvpInstances : List[Rsvpinstance]
        This property is only present if RSVP instance information was loaded 
        for the event -- see Event_Get().
    comments : str
        Event comments
    options : List[Eventoption]
        Array of event options.
    oneLineDisplay : str
        One-line display of the event information. Automatically adjusts based 
        on event type, start/end dates/times, etc.
    oneLineDisplayShort : str
        Same as oneLineDisplay, but a bit shorter
    maleGenderDisplay : str
        The display text to use for male genders on the team. This is based on 
        team settings.
    femaleGenderDisplay : str
        The display text to use for female genders on the team. This is based 
        on team settings.
    otherGenderDisplay : str
        The display text to use for other genders on the team. This is based 
        on team settings.
    dateTimeInfo : Datetimeinfo
        Simple object with describing date/time information for the event.
    location : Location
        Location object. If no properties are present, the event does not have 
        a location set.
    shirtColors : Shirtcolors
        Simple object representing the team shirt colors.
    userMetaInfo : Usermetainfo
        Simple object representing meta information about the API user in 
        context of the event's team.
    dateCreatedUtc : str
        Date/time the event was created (UTC). See important notes in the 
        Change Log (Revision 7.42) for information about this field.
    dateLastUpdatedUtc : str
        Date/time the event was last updated (UTC).
    """
    eventId: int
    team: Union[Simpleteam, dict]
    seasonId: int
    seasonName: str
    eventType: str
    eventTypeDisplay: str
    status: str
    statusDisplay: str
    personNounSingular: str
    personNounPlural: str
    title: str
    titleFull: str
    titleLabel: str
    homeAway: str
    result: Eventresult
    comments: str
    options: List #List[Eventoption] No idea whats here, need api access to figure out
    oneLineDisplay: str
    oneLineDisplayShort: str
    maleGenderDisplay: str
    femaleGenderDisplay: str
    otherGenderDisplay: str
    dateTimeInfo: Datetimeinfo
    shirtColors: Shirtcolors
    userMetaInfo: Usermetainfo
    dateCreatedUtc: str
    dateLastUpdatedUtc: str
    location: Optional[Location] = None      # This might have to be a optional. Need api access to confirm
    rsvpInstances: Optional[List[Union[Rsvpinstance, dict]]] = None
    

    def __post_init__(self):
        self.team = Simpleteam(**self.team)
        self.result = Eventresult(**self.result)
        self.rsvpInstances = [Rsvpinstance(**instance) for instance in self.rsvpInstances] if self.rsvpInstances else []
        self.dateTimeInfo = Datetimeinfo(**self.dateTimeInfo)
        self.location = Location(**self.location) if self.location else None
        self.shirtColors = Shirtcolors(**self.shirtColors)
        self.userMetaInfo = Usermetainfo(**self.userMetaInfo)
from typing import Union
from dataclasses import dataclass

from teamcowboyapi.objects.activitys import Activity

# Begin league
@dataclass
class League:
    """
    Simple object describing the league.

    Attributes:
    -----------
    leagueId : int  
        League Id
    name : str 
        League name
    city : str 
        City
    stateProvince : str 
        State/province
    postalCode : str 
        ZIP/Postal code
    countryIso2 : str 
        ISO 2-letter country code
    websiteUrl : str 
        Web site URL
    """
    leagueId: int
    name: str
    city: str
    stateProvince: str
    postalCode: str
    countryIso2: str
    websiteUrl: str


# 
# Main Parent Object
# 

@dataclass
class Season:
    """
    A schedule season (event group) that is associated with a team.

    Attributes:
    -----------
    seasonId : int
        Season Id
    teamId : int
        Team Id
    name : str
        Season name
    startDateLocal : str
        Season start date (in local time based on the timezone setting for 
        the team).
    startDateUtc : str
        Season start date in UTC.
    startDateInFuture : bool
        Whether or not the season start date is in the future.
    activity : Activity
        An activity/sport that is typically associated with teams or team 
        seasons.
    league : League
        Simple object describing the league.
    leagueDivision : str
        The team's division that is listed for the season.
    """
    seasonId: int
    teamId: int
    name: str
    startDateLocal: str
    startDateUtc: str
    startDateInFuture: bool
    activity: Activity
    league: League
    leagueDivision: str

    def __post_init__(self):
        self.activity = Activity(**self.activity)
        self.league = League(**self.league)
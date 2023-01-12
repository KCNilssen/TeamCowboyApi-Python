from typing import Optional
from dataclasses import dataclass

@dataclass
class Teammembertype:
    """
    A team member type that is assigned to a team member (or is available to 
    be assigned to a team member).

    Attributes:
    -----------
    name : str
        The internal name of the type.
    title : str
        Type title/display name
    titleShort : str
        Short version of type title/display name
    titleLongSingular : str
        Display title (long version, singular tense).
    titleLongPlural : str
        Display title (long version, plural tense).
    titleShortSingular : str
        Display title (short version, singular tense).
    titleShortPlural : str
        Display title (short version, plural tense).
    showTeamMembersOnRoster : bool
        True if team members associated with the team member type should be 
        displayed on the team roster (and in other places where the team 
        roster information is used). This setting comes from the team's 
        preferences, so it should be respected at all times when displaying 
        information.
    showTeamMembersOnAttList : bool
        True if team members associated with the team member type should be 
        displayed on the attendance list for the team's events. This setting 
        comes from the team's preferences, so it should be respected at all 
        times when displaying information.
    showTitleOnAttList : bool
        True if the display title should be shown in the attendance list for 
        the team's events. This setting comes from the team's preferences, so 
        it should be respected if at all possible.
    """
    name: str
    title: Optional[str] = None
    titleShort: Optional[str] = None
    titleLongSingular: Optional[str] = None
    titleLongPlural: Optional[str] = None
    titleShortSingular: Optional[str] = None
    titleShortPlural: Optional[str] = None
    showTeamMembersOnRoster: Optional[bool] = None
    showTeamMembersOnAttList: Optional[bool] = None
    showTitleOnAttList: Optional[bool] = None
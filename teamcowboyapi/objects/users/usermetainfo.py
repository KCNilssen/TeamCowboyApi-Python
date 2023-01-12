from typing import Optional
from dataclasses import dataclass

@dataclass
class Usermetainfo:
    """
    Simple object representing meta information about the API user in context 
    of the team that the message applies to.

    Attributes:
    -----------
    isTeamAdmin : bool 
        True if the user is a team administrator on the message’s team
    showOnDashboard : bool 
        True if the user user has selected to show the message’s team on their 
        Dashboard page
    canEdit : bool 
        True if the user can edit/delete the message
    """
    isTeamAdmin: bool
    showOnDashboard: bool
    canEdit: Optional[bool] = None
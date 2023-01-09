from dataclasses import dataclass

@dataclass
class Activity:
    """
    An activity/sport that is typically associated with teams or team seasons.
    
    Attributes:
    -----------
    activityId : int
        Activty Id
    name : str
        Activity name
    """
    activityId: int
    name: str
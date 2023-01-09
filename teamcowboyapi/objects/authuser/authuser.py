from dataclasses import dataclass

@dataclass
class Authuser:
    """
    Holds a user token for a Team Cowboy user account for use with your 
    API account. Auth_GetUserToken Response Object.

    Attributes
    ----------
    userId : int
        The ID of the user matched.
    token : str
        A unique token for the user matched. Tokens are 36-character, 
        lower-cased GUIDs.
    """
    userId: int
    token: str
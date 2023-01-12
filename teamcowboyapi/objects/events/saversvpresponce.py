from dataclasses import dataclass

@dataclass
class Saversvpresponse:
    """
    
    Attributes:
    -----------
    rsvpSaved : bool
        True if the RSVP was saved, false otherwise.
    statusCode : str
        A status code indicating why the RSVP could not be saved. This value 
        may be present if the RSVP is saved but will be blank.
 
        Possible values:
            rsvpOverTotal - The event and/or team setting has a limit on the 
                            number of “yes” RSVPs that can exist for the 
                            event, and the RSVP you attempted to save would 
                            exceed that limit
            rsvpNotAllowed - The RSVP is not allowed per event and/or team 
                            settings (rules based on the event type, team 
                            member type, etc.)
            userNotOnTeam - The user you are trying to RSVP for is not on the 
                            team indicated
            commentsOverMaxLength - The comments provided are over the maximum 
                            length (150 characters)
            generalError - Some other error occurred and the RSVP could not be 
                            saved
    """
    rsvpSaved: bool
    statusCode: str
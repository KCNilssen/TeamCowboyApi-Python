import logging

from typing import List, Union

from .tc_dataadapter import TCDataAdapter


class Teamcowboy:
    """
    A class used to retrive Teamcowboy API objects

    ...

    Attributes:
    ----------
    hostname: str
        hostname of api.teamcowboy.com
    logger: logging.Loger
        logger
    """
    def __init__(self, hostname: str = 'api.teamcowboy.com', 
        logger: logging.Logger = None):
        self._tc_adapter_v1 = TCDataAdapter(hostname, 'v1', logger)
        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)



    """
    Authentication Methods
    """

    def Auth_GetUserToken() -> Authuser:
        """
        This function makes an API call to retrieve a user auth token.
        
        Parameters:
        -----------
        
        Returns:
        --------
        A Authuser object
        """
        pass



    """
    Event Methods
    """

    def Event_Get() -> Event:
        """
        Retrieves details for a specific event. User must be an active team 
        member on the team provided and the event must be associated with the 
        team provided.
        
        Parameters:
        -----------

        Returns:
        --------
        Event object
        """
        pass

    def Event_GetAttendanceList() -> Attendancelist:
        """
        Retrieves attendance list information for a specific event. This 
        provides a list of team members and their RSVP statuses for the 
        requested event.
        
        Parameters:
        -----------

        Returns:
        --------
        Attendencelist object
        """
        pass

    def Event_SaveRSVP() -> Saversvpresponse:
        """
        Saves an event RSVP for a user. Note that rules surrounding RSVPs are 
        complex and can vary from event-level rules to more complete team 
        rules. These rules are taken into consideration when evaluating the 
        parameter values below, so some parameter values may be ignored. For 
        example, if a team does not permit additional male or female players 
        from being included in RSVPs, these values, even if provided, will be 
        ignored. Similarly, if a team does not allow certain RSVP statuses 
        such as “available”, then providing “available” as the status 
        parameter value will either throw an error or it will default to the 
        next best fit RSVP status (e.g., “maybe” or “no”).
        
        Parameters:
        -----------

        Returns:
        --------
        Saversvpresponse object
        """
        pass



    """
    Message Methods
    """

    def Message_Get() -> Message:
        """
        Retrieves information about a team message.
        
        Parameters:
        -----------

        Returns:
        --------
        Message object
        """
        pass

    def Message_Delete() -> bool:
        """
        Deletes a team message. The user attempting to delete the message must 
        be a team admin for the team that the message is associated with, or 
        they must be the author of the message.

        Request Method:        
        ---------------
        - POST
        
        Parameters:
        -----------

        Returns:
        --------
        Boolean
        """
        pass

    def Message_Save() -> Message:
        """
        Saves (adds or updates) a team message.

        Request Method:        
        ---------------
        - POST

        Parameters:
        -----------

        Returns:
        --------
        Message object that was added or updated.
        """
        pass

    def MessageComment_Delete() -> bool:
        """
        Deletes a comment for a message. The user attempting to delete the 
        comment must be a team admin for the team that the message comment 
        is associated with, or they must be the author of the comment.

        Request Method:        
        ---------------
        - POST

        Parameters:
        -----------

        Returns:
        --------
        Boolean (true if the comment was successfully deleted, false otherwise)
        """
        pass

    def MessageComment_Add() -> Messagecomment:
        """
        Adds a new comment for a message. The message must allow comments to 
        be posted or the request will not be successful.

        Request Method:        
        ---------------
        - POST

        Parameters:
        -----------

        Returns:
        --------
        MessageComment object for the comment that was added.
        """
        pass



    """
    Team Methods
    """
    
    def Team_Get() -> Team:
        """
        Retrieves information about a team. The team requested must be 
        accessible by the user represented by the user token being provided 
        (i.e., you cannot retrieve team information for a team unless the 
        user is an active member of that team).

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        Team object.
        """
        pass

    def Team_GetEvents() -> List[Event]:
        """
        Retrieves an array of events for a team's season.The team requested 
        must be accessible by the user represented by the user token being 
        provided (i.e., you cannot retrieve team information for a team unless 
        the user is an active member of that team).

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        List of Event objects.
        """
        pass

    def Team_GetMessages() -> List[Message]:
        """
        This function makes an API call to retrieve a list of messages for a 
        team.

        Request Method:        
        ---------------
        - GET
        
        Parameters:
        -----------

        Returns:
        --------
        A list of Message objects
        """
        pass

    def Team_GetRoster() -> List[User]:
        """
        Retrieves roster members for a given team.

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        Array of User objects.
        """
        pass

    def Team_GetSeasons() -> List[Season]:
        """
        Retrieves schedule seasons for a team. The team requested must be 
        accessible by the user represented by the user token being provided 
        (i.e., you cannot retrieve team information for a team unless the user 
        is an active member of that team).

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        Array of Season objects.
        """
        pass



    """
    Test Methods
    """

    def Test_GetRequest() -> Testresponce:
        """
        This is a very basic testing method for checking that you are able to 
        call the Team Cowboy API via a HTTP GET.

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        Testresponce object. 
        """
        pass

    def Test_PostRequest() -> Testresponce:
        """
        This is a very basic testing method for checking that you are able to 
        call the Team Cowboy API via a HTTP POST.

        Request Method:        
        ---------------
        - POST

        Parameters:
        -----------

        Returns:
        --------
        Testresponce object. 
        """
        pass

    """
    User Methods
    """

    def User_Get() -> User:
        """
        Retrieves user details.

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        User object.
        """
        pass

    def User_GetNextTeamEvent() -> Event:
        """
        Retrieves the next event on the user's event schedule. By default, the 
        event will be the next event from any of the teams that are visible in 
        the user's profile. The next event can be restricted to a specific 
        team by providing a value for the teamId parameter in the method call.

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        Event object. If no next event is present, an empty object will be 
        returned.
        """
        pass

    def User_GetTeamEvents() -> List[Event]:
        """
        Retrieves an array of events for the teams that the user is an active 
        member of. Events are only returned for teams that are visible in the 
        user's profile.

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        List of Event objects.
        """
        pass
    
    def User_GetTeamMessages() -> List[Message]:
        """
        Retrieves an array of Message Board posts for the teams that the user 
        is an active member of. Message Board posts are only returned for 
        teams that are visible in the user's profile.

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        List of Message objects.
        """
        pass

    def User_GetTeams() -> List[Team]:
        """
        This function makes an API call to retrieve a list of teams for a user.
        
        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------

        Returns:
        --------
        A list of Team objects
        """
        pass
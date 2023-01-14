import time
from typing import List, Union
import logging

from .exceptions import TheTeamCowboyAPIException
from .tc_dataadapter import TCDataAdapter

from teamcowboyapi import tc_helpers

from teamcowboyapi.objects.authuser import Authuser
from teamcowboyapi.objects.events import Event, Saversvpresponse
from teamcowboyapi.objects.attendances import Attendancelist
from teamcowboyapi.objects.messages import Message, Messagecomment


class Teamcowboy:
    """
    A class used to retrive Teamcowboy API objects

    ...

    Attributes:
    ----------
    privateapikey : str
        This is the private API key granted to you along with your API account.
    publicapikey : str
        This is the public API key granted to you along with your API account.
    username : str
        The username of the user you are getting a token for.
    password : str
        The password of the user you are getting a token for.
    hostname : str
        hostname of api.teamcowboy.com
    logger : logging.Loger
        logger
    """
    def __init__(self, privateapikey, publicapikey,
                    username, password,
                    hostname: str = 'api.teamcowboy.com',
                    logger: logging.Logger = None):
        self.privatekey = privateapikey
        self.publickey = publicapikey
        self.usertoken = self.Auth_GetUserToken(username, password).token
        self._tc_adapter_v1 = TCDataAdapter(hostname, 'v1', logger)
        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)


        token = self.Auth_GetUserToken(username, password)

        if token and token.token:
            self.usertoken = token.token
        else:
            raise TheTeamCowboyAPIException(f"Failed to create usertoken")


    """
    Authentication Methods
    """

    def Auth_GetUserToken(self, username: str, password: str) -> Authuser:
        """
        This function makes an API call to retrieve a user auth token.

        Request Method:        
        ---------------
        - POST
        
        Parameters:
        -----------
        username : str
            Required. The username of the user you are getting a token for.
        password : str
            Required. The password of the user you are getting a token for.

        Returns:
        --------
        A Authuser object
        """

        rdata = {
            "request_type": "POST",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "username":username,
            "password":password,
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        if "token" in tc_data and tc_data["token"]:
            return Authuser(**tc_data.data)

    """
    Event Methods
    """

    def Event_Get(self, teamId: int, eventId: int, **params) -> Event:
        """
        Retrieves details for a specific event. User must be an active team 
        member on the team provided and the event must be associated with the 
        team provided.

        Request Method:        
        ---------------
        - GET
        
        Parameters:
        -----------
        teamId : int
            Id of the team that the event is associated with.
        eventId : int
            Id of the event to retrieve.

        Optional Parameters:
        --------------------
        includeRSVPInfo : bool
            Optional. Whether or not to include RSVP information for the user.
            Default value:  false

        Returns:
        --------
        Event object
        """

        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "eventId": eventId,
            "includeRSVPInfo": includeRSVPInfo
        }

        rdata |+ params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        if "eventId" in tc_data.data and tc_data.data["eventId"]:
            return Event(**tc_data.data)

    def Event_GetAttendanceList(self, teamId: int, eventId: int) -> Attendancelist:
        """
        Retrieves attendance list information for a specific event. This 
        provides a list of team members and their RSVP statuses for the 
        requested event.

        Request Method:        
        ---------------
        - GET
        
        Parameters:
        -----------
        teamId : int
            Id of the team that the event is associated with.
        eventId : int
            Id of the event for the attendance list to retrieve.

        Returns:
        --------
        Attendencelist object
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "eventId": eventId,
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        if "users" in tc_data.data and tc_data.data["users"]:
            return Attendancelist(**tc_data.data)

    def Event_SaveRSVP(self, teamId: int, eventId: int, status: str, 
                        **params) -> Saversvpresponse:
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

        Request Method:        
        ---------------
        - POST
        
        Parameters:
        -----------
        teamId : int
            Id of the team that the event is associated with.
        eventId : int
            Id of the event to retrieve.
        status : str 
            The RSVP status to save for the user.
            To remove a RSVP, pass “noresponse” to remove the RSVP (if RSVP 
            removal is allowed for the event). To determine if RSVP removal is 
            allowed for a given event, refer to 
            Event.rsvpInstances[].rsvpDetails.allowRsvpRemoval
            Valid values:  yes, maybe, available, no, noresponse

        Optional Parameters:
        --------------------
        addlMale : int
            Optional. The number of additional male players to include as 
            “yes” in the RSVP. If this parameter is omitted from the request, 
            any value present for additional male players on the RSVP is not 
            updated (i.e., existing values will not be overwritten). To remove 
            this value for the RSVP, pass 0 (zero).
        addlFemale : int
            Optional. The number of additional female players to include as 
            “yes” in the RSVP. If this parameter is omitted from the request, 
            any value present for additional female players on the RSVP is not 
            updated (i.e., existing values will not be overwritten). To remove 
            this value for the RSVP, pass 0 (zero).
        comments : str
            Optional. RSVP comments. If not provided, any existing RSVP 
            comments will be cleared out for the user's RSVP.
        rsvpAsUserId : int
            Optional. The user to RSVP for. This is used to allow a user to 
            RSVP as a user that is in their list of linked users. If not 
            provided, the RSVP will be saved for the user associated with the 
            userToken parameter value.

        Returns:
        --------
        Saversvpresponse object
        """

        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "eventId": eventId,
            "status": status
        }

        rdata |+ params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        if "users" in tc_data.data and tc_data.data["users"]:
            return Attendancelist(**tc_data.data)


    """
    Message Methods
    """

    def Message_Get(self, teamId: int, messageId: int, **params) -> Message:
        """
        Retrieves information about a team message.

        Request Method:        
        ---------------
        - GET
        
        Parameters:
        -----------
        teamId : int
            Id of the team associated with the message.
        messageId : int
            Id of the message to retrieve.

        Optional Parameters:
        --------------------
        loadComments : bool
            Optional. Whether or not to load comments for the message.
            Default value: false

        Returns:
        --------
        Message object
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
        }

        rdata |+ params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        if "messageId" in tc_data.data and tc_data.data["messageId"]:
            return Message(**tc_data.data)

    def Message_Delete(self, teamId: int, messageId: int) -> bool:
        """
        Deletes a team message. The user attempting to delete the message must 
        be a team admin for the team that the message is associated with, or 
        they must be the author of the message.

        Request Method:        
        ---------------
        - POST
        
        Parameters:
        -----------
        teamId : int
            Id of the team associated with the message.
        messageId : int
            Id of the message to delete.

        Returns:
        --------
        Boolean
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        # Responce is a bool, so just return responce?
        return tc_data.data

    def Message_Save(self, teamId: int, title: str, body: str, **params) -> Message:
        """
        Saves (adds or updates) a team message.

        Request Method:        
        ---------------
        - POST

        Parameters:
        -----------
        teamId : int
            Id of the team associated with the message to add/update.
        title : str 
            The title of the message.
        body : str
            The body of the message. HTML is allowed, although unsafe tags are 
            stripped out (nearly all normal HTML tags are allowed).

        Optional Parameters:
        --------------------
        messageId : int
            Optional. Id of the message to update. If not provided, a new 
            message will be added.
        isPinned : bool
            Optional. Whether or not the message should be pinned in the 
            team's list of mesages.
            Default value:  false (this value is forced to false if the user 
            adding/updating the message is not a team admin).
        sendNotifications : bool
            Optional. Whether or not to send notifications when the message 
            and any message comments are posted.
            Default value:  false
        isHidden : bool
            Optional. Whether or not the message is hidden in the team's list 
            of messages.
            Default value:  false (this value is forced to false if the user 
            adding/updating the message is not a team admin).
        allowComments : bool
            Optional. Whether or not comments can be posted for the message.
            Default value:  true

        Returns:
        --------
        Message object that was added or updated.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "title": title,
            "body": body
        }

        rdata |+ params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        if "messageId" in tc_data.data and tc_data.data["messageId"]:
            return Message(**tc_data.data)


    def MessageComment_Delete(self, teamId: int, messageId: int, commentId: int) -> bool:
        """
        Deletes a comment for a message. The user attempting to delete the 
        comment must be a team admin for the team that the message comment 
        is associated with, or they must be the author of the comment.

        Request Method:        
        ---------------
        - POST

        Parameters:
        -----------
        teamId : int
            Id of the team associated with the message.
        messageId : int
            Id of the message that the comment is associated with.
        commentId : int
            Id of the comment to delete.

        Returns:
        --------
        Boolean (true if the comment was successfully deleted, false otherwise)
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
            "commentId": commentId
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        # Responce is a bool, so just return responce?
        return tc_data.data


    def MessageComment_Add(self, teamId: int, messageId: int, comment: str) -> Messagecomment:
        """
        Adds a new comment for a message. The message must allow comments to 
        be posted or the request will not be successful.

        Request Method:        
        ---------------
        - POST

        Parameters:
        -----------
        teamId : int
            Id of the team associated with the message.
        messageId : int
            Id of the message that the comment is associated with.
        comment : str
            The text of the comment being added.

        Returns:
        --------
        MessageComment object for the comment that was added.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Auth_GetUserToken",
            "timestamp":time.time(),
            "nonce":F"int(1000*{time.time()})",
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
            "comment": comment
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'https://api.teamcowboy.com/v1/', data = request_data).json

        if "commentId" in tc_data.data and tc_data.data["commentId"]:
            return Messagecomment(**tc_data.data)



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
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
from teamcowboyapi.objects.teams import Team
from teamcowboyapi.objects.users import User
from teamcowboyapi.objects.seasons import Season
from teamcowboyapi.objects.tests import Tresponce


class Teamcowboy:
    """
    A class used to retrive Teamcowboy API objects
    
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
        self._tc_adapter_v1 = TCDataAdapter(hostname, 'v1', logger)
        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

        self.privatekey = privateapikey
        self.publickey = publicapikey
        # self.usertoken = self.Auth_GetUserToken(username, password).token

        token = self.Auth_GetUserToken(username, password)

        if token:
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
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "username":username,
            "password":password,
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'', data = request_data)

        if "token" in tc_data.data and tc_data.data["token"]:
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
        includeRSVPInfo : str
            Optional. Whether or not to include RSVP information for the user.
            Default value:  false
            Options: True, False

        Returns:
        --------
        Event object
        """

        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Event_Get",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "eventId": eventId            
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

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
            "method":"Event_GetAttendanceList",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "eventId": eventId,
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

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
            "request_type": "POST",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Event_SaveRSVP",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "eventId": eventId,
            "status": status
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'', data = request_data)

        if "rsvpSaved" in tc_data.data and tc_data.data["rsvpSaved"]:
            return Saversvpresponse(**tc_data.data)


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
        loadComments : str
            Optional. Whether or not to load comments for the message.
            Default value: "false"
            Accepted values: "False", "True"
        Returns:
        --------
        Message object
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Message_Get",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

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
            "request_type": "POST",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Message_Delete",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'', data = request_data)

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
            "request_type": "POST",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Message_Save",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "title": title,
            "body": body
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'', data = request_data)

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
            "request_type": "POST",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"MessageComment_Delete",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
            "commentId": commentId
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'', data = request_data)

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
            "method":"MessageComment_Add",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,
            "messageId": messageId,
            "comment": comment
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'', ep_params = request_data)

        if "commentId" in tc_data.data and tc_data.data["commentId"]:
            return Messagecomment(**tc_data.data)



    """
    Team Methods
    """
    
    def Team_Get(self, teamId: int) -> Team:
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
        teamId : int
            Id of the team to retrieve.

        Returns:
        --------
        Team object.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Team_Get",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,            
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if "teamId" in tc_data.data and tc_data.data["teamId"]:
            return Team(**tc_data.data)

    def Team_GetEvents(self, teamId: int, **params) -> List[Event]:
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
        teamId : int
            Id of the team to retrieve events for.

        Optional Parameters:
        --------------------
        seasonId : int
            Optional. Id of the season to retrieve events for.
            If not provided, events for all of the team's seasons will be 
            returned.
        offset : int
            Optional. The number of events to shift from those returned. This 
            is typically used if you are requesting a specific number of 
            events per page and you need to offset to a different page. This 
            value is zero-based (i.e., for no offset, use 0, not 1).
            Default value:  0
        qty : int
            Optional. The number of events to retrieve. Again, if using 
            pagination in your application, this would typically be the page 
            size, or you just want to reduce the response size (i.e., less 
            events).
            Default value:  10
        filter : str
            Optional. An enumeration value indicating a special filter for 
            retrieving events.
            Valid values:
                - past - returns events that have a start date before the 
                    current date in the team's time zone
                - future - returns events that start in the future, based on 
                    the current date/time in the team's time zone
                - specificDates - returns events bounded by a specific date 
                    range, specified by the “startDateTime” and “endDateTime” 
                    parameters. At least one of these parameters is required if 
                    using this filter value.
                - nextEvent - returns the next event based on the current 
                    date/time. Note that this keys off of the start date/time 
                    of the event.
                - previousEvent - returns the previous event based on the 
                    current date/time. Note that this keys off of the start 
                    date/time of the event.
            If not provided, the filter defaults to “future”.
        startDateTime : str
            Required (if filter=specificDates). If provided, events will only 
            be retrieved that have a start date on or after this value. The 
            value provided is evaluated against the local date for the event.
            Enter date/time in format:
            YYYY-MM-DD HH:MM:SS
        endDateTime : str
            Required (if filter=specificDates). If provided, events will only 
            be retrieved that have a start date on or before this value. The 
            value provided is evaluated against the local date for the event.
            Enter date/time in format:
            YYYY-MM-DD HH:MM:SS

        Returns:
        --------
        List of Event objects.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Team_GetEvents",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,            
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if tc_data.data:
            return [Event(**event) for event in tc_data.data]

    def Team_GetMessages(self, teamId: int, **params) -> List[Message]:
        """
        This function makes an API call to retrieve a list of messages for a 
        team.

        Request Method:        
        ---------------
        - GET
        
        Parameters:
        -----------
        teamId : int
            Id of the team to retrieve messages for.

        Opional Parameters:
        -------------------
        messageId : int
            Optional. Id of the message to retrieve. If not provided, all 
            messages are retrieved.
        offset : int
            Optional. The number of messages to shift from those returned. 
            This is typically used if you are requesting a specific number of 
            messages per page. This value is zero-based (i.e., for no offset, 
            use 0, not 1).
            Default value:  0
        qty : int
            Optional. The number of messages to retrieve. Again, if using 
            pagination in your application, this would typically be the page 
            size.
            Default value:  10
        sortBy : str
            Optional. An enumeration value indicating how to sort the messages 
            that are returned.
            Valid values:
                - title - message title
                - lastUpdated - date/time when the message was last updated
                - type - the message type (pinned or regular message)
            Default value:  lastUpdated
        sortDirection : str
            Optional. The sort direction for the messages returned.
            Valid values:  ASC, DESC
            Default value:  The default value varies based on the sortBy 
            parameter:
                - title: ASC
                - lastUpdated: DESC
                - type: DESC
                - No sortBy parameter: ASC

        Returns:
        --------
        A list of Message objects
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Team_GetMessages",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,            
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if tc_data.data:
            return [Message(**msg) for msg in tc_data.data]

    def Team_GetRoster(self, teamId: int, **params) -> List[User]:
        """
        Retrieves roster members for a given team.

        Request Method:        
        ---------------
        - GET

        Parameters:
        -----------
        teamId : int
            Id of the team to retrieve.

        Optional Parameters:
        --------------------
        userId : int
            Optional. Id of a specific user/team member to retrieve. If 
            omitted, all team members are returned.
        includeInactive : bool
            Optional. Whether or not to include team members that are marked 
            as “inactive” for a team (inactive team members cannot access the 
            team but are visible from the Roster page for team admins). 
            Default value:  true
        sortBy : str
            Optional. Order to sort the team members returned. The valid 
            values for this parameter vary depending on whether or not the 
            user making the method call is an admin on the team.
            Valid values (case-sensitive):
                - If user is a team admin:  playerType, playerType_sex, sex, 
                sex_playerType, email, email2, firstName, lastName, phone, 
                tshirtSize, tshirtNumber, pantsSize, lastLogin, active, 
                inviteStatus
                - If user is not a team admin:  firstName, playerType, sex
            Default value:  firstName
        sortDirection : str
            Optional. The sort direction for the team members returned.
            Valid values:  ASC, DESC
            Default value:  ASC

        Returns:
        --------
        Array of User objects.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Team_GetRoster",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,            
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if tc_data.data:
            return [User(**user) for user in tc_data.data]

    def Team_GetSeasons(self, teamId: int) -> List[Season]:
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
        teamId : int
            Id of the team to retrieve seasons for.

        Returns:
        --------
        Array of Season objects.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Team_GetSeasons",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,
            "teamId": teamId,            
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if tc_data.data:
            return [Season(**season) for season in tc_data.data]


    """
    Test Methods
    """

    def Test_GetRequest(self, **params) -> Tresponce:
        """
        This is a very basic testing method for checking that you are able to 
        call the Team Cowboy API via a HTTP GET.

        Request Method:        
        ---------------
        - GET

        Optional Parameters:
        -----------
        testParam : str
            Optional. A string to send with the method. The value will be 
            output in the response so you can verify that you sent a 
            parameter successfully.

        Returns:
        --------
        Testresponce object. 
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Test_GetRequest",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json"    
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if "helloWorld" in tc_data.data and tc_data.data["helloWorld"]:
            return Tresponce(**tc_data.data)
        

    def Test_PostRequest(self, **params) -> Tresponce:
        """
        This is a very basic testing method for checking that you are able to 
        call the Team Cowboy API via a HTTP POST.

        Request Method:        
        ---------------
        - POST

        Optional Parameters:
        -----------
        testParam : str
            Optional. A string to send with the method. The value will be 
            output in the response so you can verify that you sent a 
            parameter successfully.

        Returns:
        --------
        Testresponce object. 
        """
        
        rdata = {
            "request_type": "POST",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"Test_PostRequest",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json"    
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.post(endpoint=f'', data = request_data)

        if "helloWorld" in tc_data.data and tc_data.data["helloWorld"]:
            return Tresponce(**tc_data.data)
        

    """
    User Methods
    """

    def User_Get(self) -> User:
        """
        Retrieves user details.

        Request Method:        
        ---------------
        - GET

        Returns:
        --------
        User object.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"User_Get",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken,          
        }

        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if "userId" in tc_data.data and tc_data.data["userId"]:
            return User(**tc_data.data)

    def User_GetNextTeamEvent(self, **params) -> Event:
        """
        Retrieves the next event on the user's event schedule. By default, the 
        event will be the next event from any of the teams that are visible in 
        the user's profile. The next event can be restricted to a specific 
        team by providing a value for the teamId parameter in the method call.

        Request Method:        
        ---------------
        - GET

        Optional Parameters:
        --------------------
        teamId : int
            Optional. A teamId to restrict the event returned to a specific 
            team. If not provided, events for all of the user's teams will be 
            considered.
        dashboardTeamsOnly : bool
            Optional. Whether or not to only consider the user's Dashboard 
            teams when retrieving the user's next event.
            Default value:  false

        Returns:
        --------
        Event object. If no next event is present, an empty object will be 
        returned.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"User_GetNextTeamEvent",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken        
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if "eventId" in tc_data.data and tc_data.data["eventId"]:
            return Event(**tc_data.data)

    def User_GetTeamEvents(self, **params) -> List[Event]:
        """
        Retrieves an array of events for the teams that the user is an active 
        member of. Events are only returned for teams that are visible in the 
        user's profile.

        Request Method:        
        ---------------
        - GET

        Optional Parameters:
        --------------------
        startDateTime : str
            Optional. If provided, events will only be retrieved that have a 
            start date/time on or after this value. The value provided is 
            evaluated against the local date/time for the event. If not 
            provided, the current date/time is used.
            Enter date/time in format:
            YYYY-MM-DD HH:MM:SS
        endDateTime : str
            Optional. If provided, events will only be retrieved that have a 
            start date/time on or before this value. The value provided is 
            evaluated against the local date/time for the event. If not 
            provided, the current date/time + 60 days is used.
            Enter date/time in format:
            YYYY-MM-DD HH:MM:SS
        teamId : int
            Optional. A teamId to restrict the events returned to a specific 
            team. If not provided, events for all of the user's teams are 
            returned.
        dashboardTeamsOnly : bool
            Optional. Whether or not to restrict the events retrieved only to 
            those for teams on the user's Dashboard.
            Default value:  false

        Returns:
        --------
        List of Event objects.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"User_GetTeamEvents",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken        
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if tc_data.data:
            return [Event(**event) for event in tc_data.data]
    
    def User_GetTeamMessages(self, **params) -> List[Message]:
        """
        Retrieves an array of Message Board posts for the teams that the user 
        is an active member of. Message Board posts are only returned for 
        teams that are visible in the user's profile.

        Request Method:        
        ---------------
        - GET

        Optional Parameters:
        --------------------
        teamId : int
            Optional. A teamId to restrict the messages that are returned to a 
            specific team.
            Default:  If this value is not provided, messages for all of the 
            user's teams are returned.
        messageId : int
            Optional. Id of the message to retrieve. If not provided, all 
            messages are retrieved.
        offset : int
            Optional. The number of messages to shift from those returned. 
            This is typically used if you are requesting a specific number of
            messages per page. This value is zero-based (i.e., for no offset, 
            use 0, not 1).
            Default value:  0
        qty : int
            Optional. The number of messages to retrieve. Again, if using 
            pagination in your application, this would typically be the page 
            size.
            Default value:  10
        sortBy : str
            Optional. An enumeration value indicating how to sort the messages 
            that are returned.
            Valid values:
                - title - message title
                - lastUpdated - date/time when the message was last updated
                - type - the message type (pinned or regular message)
            Default value:  lastUpdated
        sortDirection : str
            Optional. The sort direction for the messages returned.
            Valid values:  ASC, DESC
            Default value:  The default value varies based on the sortBy parameter:
                - title: ASC
                - lastUpdated: DESC
                - type: DESC
                - No sortBy parameter: ASC

        Returns:
        --------
        List of Message objects.
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"User_GetTeamMessages",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken        
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if tc_data.data:
            return [Message(**messsage) for messsage in tc_data.data]

    def User_GetTeams(self, **params) -> List[Team]:
        """
        This function makes an API call to retrieve a list of teams for a user.
        
        Request Method:        
        ---------------
        - GET

        Optional Parameters:
        --------------------
        dashboardTeamsOnly : bool
            Optional. Whether or not to restrict the teams retrieved only to 
            those on the user's Dashboard.
            Default value:  false

        Returns:
        --------
        A list of Team objects
        """
        
        rdata = {
            "request_type": "GET",
            "private_key":self.privatekey,
            "api_key":self.publickey,
            "method":"User_GetTeams",
            "timestamp":int(time.time()),
            "nonce":"{:.4f}".format(time.time()),
            "responce_type":"json",
            "userToken": self.usertoken        
        }

        rdata |= params
        request_data = tc_helpers.createrequestdata(rdata)

        tc_data = self._tc_adapter_v1.get(endpoint=f'', ep_params = request_data)

        if tc_data.data:
            return [Team(**team) for team in tc_data.data]
import unittest
# from dotenv import load_dotenv
import os 

from datetime import datetime

from teamcowboyapi import Teamcowboy

from teamcowboyapi.objects.authuser import Authuser
from teamcowboyapi.objects.events import Event, Saversvpresponse
from teamcowboyapi.objects.attendances import Attendancelist
from teamcowboyapi.objects.messages import Message, Messagecomment
from teamcowboyapi.objects.teams import Team
from teamcowboyapi.objects.users import User
from teamcowboyapi.objects.seasons import Season
from teamcowboyapi.objects.tests import Tresponce


class TestAuth(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # load_dotenv()
        privateapikey = os.environ.get("PRIVATEAPIKEY")
        publicapikey = os.environ.get("PUBLICAPIKEY")
        username = os.environ.get("USERNAME")
        password = os.environ.get("PASSWORD")

        # print (privateapikey, publicapikey, username, password)
        cls.tc = Teamcowboy(privateapikey= privateapikey, publicapikey= publicapikey, username= username, password= password)
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_auth_getusertoken(self):
        """
        Tests Auth_GetUserToken function with teamcowboy api
        """
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        authreturn = self.tc.Auth_GetUserToken(username, password)

        # authreturn should not be none
        self.assertIsNotNone(authreturn)
        # Returned item should be a Authuser object
        self.assertIsInstance(authreturn, Authuser)

    def test_event_get(self):
        """
        Tests Event_Get function with teamcowboy api
        """
        # Event_Get(self, teamId: int, eventId: int, **params) -> Event:
        teamid = 208
        event1Id = 1950161 # bye game
        event2Id = 1950162 # game vs sharks
        includeRSVPInfo = "False"
        
        event1getreturn = self.tc.Event_Get(teamid, event1Id, includeRSVPInfo=includeRSVPInfo)
        event2getreturn = self.tc.Event_Get(teamid, event2Id, includeRSVPInfo=includeRSVPInfo)

        # eventgetreturn should not be none
        self.assertIsNotNone(event1getreturn)
        self.assertIsNotNone(event2getreturn)
        # Returned item should be a Event object
        self.assertIsInstance(event1getreturn, Event)
        self.assertIsInstance(event2getreturn, Event)

    def test_event_getattendancelist(self):
        """
        Tests Event_GetAttendanceList function with teamcowboy api
        """
        # Event_GetAttendanceList(self, teamId: int, eventId: int) -> Attendancelist:
        teamid = 208
        event1Id = 1950161 # bye game
        event2Id = 1950162 # game vs sharks
        
        attendancelist1return = self.tc.Event_GetAttendanceList(teamid, event1Id)
        attendancelist2return = self.tc.Event_GetAttendanceList(teamid, event2Id)

        # attendancelistreturn should not be none
        self.assertIsNotNone(attendancelist1return)
        self.assertIsNotNone(attendancelist2return)
        # Returned item should be a Attendancelist object
        self.assertIsInstance(attendancelist1return, Attendancelist)
        self.assertIsInstance(attendancelist2return, Attendancelist)

    def test_event_saversvp(self):
        """
        Tests Event_SaveRSVP function with teamcowboy api
        """
        # Event_SaveRSVP(self, teamId: int, eventId: int, status: str, **params) -> Saversvpresponse:
        # teamid = 208
        # event2Id = 1950162 # game vs sharks
        # status = "yes"
        # # addlMale = 
        # # addlFemale = 
        # # comments =
        # # rsvpAsUserId = 
        
        # saversvpresponce = self.tc.Event_SaveRSVP(teamid, event2Id, status)

        # # saversvpresponce should not be none
        # self.assertIsNotNone(saversvpresponce)
        # # Returned item should be a Saversvpresponse object
        # self.assertIsInstance(saversvpresponce, Saversvpresponse)

    def test_message_get(self):
        """
        Tests Message_Get function with teamcowboy api
        """
        # Message_Get(self, teamId: int, messageId: int, **params) -> Message:
        teamid = 208
        messageId = 137756
        loadComments = "False"
        
        messsagegetresponce = self.tc.Message_Get(teamid, messageId, loadComments=loadComments)

        # messsagegetresponce should not be none
        self.assertIsNotNone(messsagegetresponce)
        # Returned item should be a Message object
        self.assertIsInstance(messsagegetresponce, Message)

    def test_message_delete(self):
        """
        Tests Message_Delete function with teamcowboy api
        """
        # Message_Delete(self, teamId: int, messageId: int) -> bool:
        # teamid = 208
        # messageId = 1234
        
        # messsagedeleteresponce = self.tc.Message_Get(teamid, messageId)

        # # messsagedeleteresponce should not be none
        # self.assertIsNotNone(messsagedeleteresponce)
        # # messsagedeleteresponce item should be a bool
        # self.assertIsInstance(messsagedeleteresponce, bool)

    def test_message_save(self):
        """
        Tests Message_Save function with teamcowboy api
        """
        # # Message_Save(self, teamId: int, title: str, body: str, **params) -> Message:
        # teamid = 208
        # messageId = 1234
        # body = "This is the body text for testing"
        # # messageId = 
        # # isPinned = 
        # # sendNotifications = 
        # # isHidden = 
        # # allowComments =        
        
        # messsagesaveresponce = self.tc.Message_Save(teamid, messageId, body)

        # # messsagesaveresponce should not be none
        # self.assertIsNotNone(messsagesaveresponce)
        # # messsagesaveresponce item should be a Message
        # self.assertIsInstance(messsagesaveresponce, Message)

    def test_messagecomment_delete(self):
        """
        Tests Message_Save function with teamcowboy api
        """
        # # MessageComment_Delete(self, teamId: int, messageId: int, commentId: int) -> bool:
        # teamid = 208
        # messageId = 1234
        # commentId = 1      
        
        # messsagecommentdeleteresponce = self.tc.MessageComment_Delete(teamid, messageId, commentId)

        # # messsagecommentdeleteresponce should not be none
        # self.assertIsNotNone(messsagecommentdeleteresponce)
        # # messsagecommentdeleteresponce item should be a Message
        # self.assertIsInstance(messsagecommentdeleteresponce, Message)

    def test_messagecomment_add(self):
        """
        Tests Message_Save function with teamcowboy api
        """
        # # MessageComment_Add(self, teamId: int, messageId: int, comment: str) -> Messagecomment:
        # teamid = 208
        # messageId = 1234
        # comment = "This is a comment to test"     
        
        # messsagecommentaddresponce = self.tc.MessageComment_Add(teamid, messageId, comment)

        # # messsagecommentaddresponce should not be none
        # self.assertIsNotNone(messsagecommentaddresponce)
        # # messsagecommentaddresponce item should be a Messagecomment
        # self.assertIsInstance(messsagecommentaddresponce, Messagecomment)

    def test_team_get(self):
        """
        Tests Message_Save function with teamcowboy api
        """
        # Team_Get(self, teamId: int) -> Team:
        teamid = 208     
        
        teamgetresponce = self.tc.Team_Get(teamid)

        # teamgetresponce should not be none
        self.assertIsNotNone(teamgetresponce)
        # teamgetresponce item should be a Team
        self.assertIsInstance(teamgetresponce, Team)
    
    def test_team_getevents(self):
        """
        Tests Team_GetEvents function with teamcowboy api
        """
        # Team_GetEvents(self, teamId: int, **params) -> List[Event]:
        teamid = 208     
        # seasonId = 
        # offset = 
        # qty = 
        # filter = 
        # startDateTime = 
        # endDateTime = 
        
        teamgeteventsresponce = self.tc.Team_GetEvents(teamid)

        # teamgeteventsresponce should not be none
        self.assertIsNotNone(teamgeteventsresponce)
        # teamgeteventsresponce item should be a List
        self.assertIsInstance(teamgeteventsresponce, list)
        # teamgeteventsresponce item should be a List of events
        self.assertIsInstance(teamgeteventsresponce[0], Event)

    def test_team_getmessages(self):
        """
        Tests Team_GetMessages function with teamcowboy api
        """
        # Team_GetMessages(self, teamId: int, **params) -> List[Message]:
        teamid = 208     
        # messageId = 
        # offset = 
        # qty = 
        # sortBy = 
        # sortDirection = 
        
        teamgetmessagesresponce = self.tc.Team_GetMessages(teamid)

        # teamgetmessagesresponce should not be none
        self.assertIsNotNone(teamgetmessagesresponce)
        # teamgetmessagesresponce item should be a List
        self.assertIsInstance(teamgetmessagesresponce, list)
        # teamgetmessagesresponce item should be a List of messages
        self.assertIsInstance(teamgetmessagesresponce[0], Message)

    def test_team_getroster(self):
        """
        Tests Team_GetRoster function with teamcowboy api
        """
        # Team_GetRoster(self, teamId: int, **params) -> List[User]:
        teamid = 208     
        # userId = 
        # includeInactive = 
        # sortBy = 
        # sortDirection =  
        
        teamgetrosterresponce = self.tc.Team_GetRoster(teamid)

        # teamgetrosterresponce should not be none
        self.assertIsNotNone(teamgetrosterresponce)
        # teamgetrosterresponce item should be a List
        self.assertIsInstance(teamgetrosterresponce, list)
        # teamgetrosterresponce item should be a List of users
        self.assertIsInstance(teamgetrosterresponce[0], User)

    def test_team_getseasons(self):
        """
        Tests Team_GetSeasons function with teamcowboy api
        """
        # Team_GetSeasons(self, teamId: int) -> List[Season]:
        teamid = 208     
        
        teamgetseasonsresponce = self.tc.Team_GetSeasons(teamid)

        # teamgetseasonsresponce should not be none
        self.assertIsNotNone(teamgetseasonsresponce)
        # teamgetseasonsresponce item should be a List
        self.assertIsInstance(teamgetseasonsresponce, list)
        # teamgetseasonsresponce item should be a List of seasons
        self.assertIsInstance(teamgetseasonsresponce[0], Season)

    def test_test_getrequest(self):
        """
        Tests Test_GetRequest function with teamcowboy api
        """
        authreturn = self.tc.Test_GetRequest(testParam="test")
        self.assertIsInstance(authreturn, Tresponce)

    def test_postrequest(self):
        """
        Tests Test_PostRequest function with teamcowboy api
        """
        authreturn = self.tc.Test_PostRequest(testParam="test")
        self.assertIsInstance(authreturn, Tresponce)

    def test_user_get(self):
        """
        Tests User_Get function with teamcowboy api
        """
        # User_Get(self) -> User: 
        usergetresponce = self.tc.User_Get()

        # usergetresponce should not be none
        self.assertIsNotNone(usergetresponce)        
        # usergetresponce item should be a user
        self.assertIsInstance(usergetresponce, User)

    def test_user_getnextteamevent(self):
        """
        Tests User_GetNextTeamEvent function with teamcowboy api
        """
        # User_GetNextTeamEvent(self, **params) -> Event:

        # teamId = 
        # dashboardTeamsOnly = 

        usergetnextteameventresponce = self.tc.User_GetNextTeamEvent()

        # usergetnextteameventresponce should not be none
        self.assertIsNotNone(usergetnextteameventresponce)        
        # usergetnextteameventresponce item should be a event
        self.assertIsInstance(usergetnextteameventresponce, Event)


    def test_user_getteamevents(self):
        """
        Tests User_GetTeamEvents function with teamcowboy api
        """
        # User_GetTeamEvents(self, **params) -> List[Event]:

        startDateTime = datetime.now()
        endDateTime = "2023-01-23 23:59:59"
        endDateTime= datetime.strptime(endDateTime, '%Y-%m-%d %H:%M:%S')
        # teamId = 
        # dashboardTeamsOnly =  
        
        usergetteameventsresponce = self.tc.User_GetTeamEvents(teamId=208)

        # usergetteameventsresponce should not be none
        self.assertIsNotNone(usergetteameventsresponce)
        # usergetteameventsresponce item should be a List
        self.assertIsInstance(usergetteameventsresponce, list)
        # usergetteameventsresponce item should be a List of events
        self.assertIsInstance(usergetteameventsresponce[0], Event)

    def test_user_getteammessages(self):
        """
        Tests User_GetTeamMessages function with teamcowboy api
        """
        # User_GetTeamMessages(self, **params) -> List[Message]:
        
        # startDateTime = 
        # endDateTime = 
        # teamId = 
        # dashboardTeamsOnly =  
        
        usergetteammessagesresponce = self.tc.User_GetTeamMessages()

        # usergetteammessagesresponce should not be none
        self.assertIsNotNone(usergetteammessagesresponce)
        # usergetteammessagesresponce item should be a List
        self.assertIsInstance(usergetteammessagesresponce, list)
        # usergetteammessagesresponce item should be a List of messages
        self.assertIsInstance(usergetteammessagesresponce[0], Message)

    def test_user_getteam(self):
        """
        Tests User_GetTeams function with teamcowboy api
        """
        # User_GetTeams(self, **params) -> List[Team]:
        
        # startDateTime = 
        # endDateTime = 
        # teamId = 
        # dashboardTeamsOnly =  
        
        usergetteamsresponce = self.tc.User_GetTeams()

        # usergetteamsresponce should not be none
        self.assertIsNotNone(usergetteamsresponce)
        # usergetteamsresponce item should be a List
        self.assertIsInstance(usergetteamsresponce, list)
        # usergetteamsresponce item should be a List of teams
        self.assertIsInstance(usergetteamsresponce[0], Team)

    
    

        

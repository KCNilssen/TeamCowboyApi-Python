<div align="center">

# Team Cowboy API Python

**The Unofficial Python Wrapper for the Team Cowboy API**

<!-- ![Development Branch Status]() -->
<!-- ![Periodic External Test Status]() -->
[![PyPI version](https://badge.fury.io/py/python-teamcowboy-api.svg)](https://badge.fury.io/py/python-teamcowboy-api)
![Main Branch Status](https://github.com/KCNilssen/TeamCowboyApi-Python/actions/workflows/build-and-test.yml/badge.svg?event=push)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-teamcowboy-api)
![GitHub](https://img.shields.io/github/license/KCNilssen/TeamCowboyApi-Python)

![Team Cowboy API](https://static.teamcowboy.com/images/tcLogo_glow.png)

<div align="left">

## Getting Started

*TeamCowboyApi-Python* is a Python library that provides developers with access to the Team Cowboy API which allows developers to retrieve information related to teams, players, events, and more. *TeamCowboyApi-Python* written in python 3.10+.

To get started with the library, refer to the information provided in this README. For a more detailed explanation, check out the documentation and the Wiki section. The Wiki contains information on return objects, endpoint structure, usage examples, and more. It is a valuable resource for getting started, working with the library, and finding the information you need. You can also visit Team Cowboys official api documentation [here](http://api.teamcowboy.com/v1/docs/#_Toc372547893) and apply for api access [here](https://www.teamcowboy.com/api/requestAccount)


<div align="center">

### [Docs](http://api.teamcowboy.com/v1/docs/) | [Examples]() | [Wiki](http://api.teamcowboy.com/v1/docs/) | [API](https://api.teamcowboy.com/v1/) 

<div align="left">

## Installation
- To be added, does not work yet
```python
python3 -m pip install python-teamcowboy-api
```

## Usage
```python
python3
>>> import teamcowboyapi
>>> Teamcowboy = teamcowboyapi.Teamcowboy(privateapikey, publicapikey, username, password)
>>> Teamcowboy.Event_Get(teamid, eventid)
```

## Documentation

### [Authentication Methods]()
* `Teamcowboy.Auth_GetUserToken(self, username: str, password: str)` - Return user auth token 
### [Event Methods]()
* `Teamcowboy.Event_Get(self, teamId: int, eventId: int, **params)` - Return Event from teamid and eventid 
* `Teamcowboy.Event_GetAttendanceList(self, teamId: int, eventId: int)` - Return Attendance List from teamid and eventid
* `Teamcowboy.Event_SaveRSVP(self, teamId: int, eventId: int, status: str, **params)` - Save RSVP from teamid eventid and rsvp status
### [Message Methods]()
* `Teamcowboy.Message_Get(self, teamId: int, messageId: int, **params)` - Return Message from teamid and messageid 
* `Teamcowboy.Message_Delete(self, teamId: int, messageId: int)` - Delete Message from teamid and messageid 
* `Teamcowboy.Message_Save(self, teamId: int, title: str, body: str, **params)` - Save Message from teamid and messageid 
* `Teamcowboy.MessageComment_Delete(self, teamId: int, messageId: int, commentId: int)` - Delete Message comment from teamid and messageid and comment
* `Teamcowboy.MessageComment_Add(self, teamId: int, messageId: int, comment: str)` - Add Message comment from teamid and messageid and comment
### [Team Methods]()
* `Teamcowboy.Team_Get(self, teamId: int)` - Return Team from teamid
* `Teamcowboy.Team_GetEvents(self, teamId: int, **params)` - Return team Events from teamid
* `Teamcowboy.Team_GetMessages(self, teamId: int, **params)` - Return team Messages from teamid
* `Teamcowboy.Team_GetRoster(self, teamId: int, **params)` - Return team Roster from teamid
* `Teamcowboy.Team_GetSeasons(self, teamId: int)` - Return team Seasons from teamid
### [Test Methods]()
* `Teamcowboy.Test_GetRequest(self, **params)` - Test api's GET
* `Teamcowboy.Test_PostRequest(self, **params)` - Test api's POST
### [User Methods]()
* `Teamcowboy.User_Get(self)` - Return User
* `Teamcowboy.User_GetNextTeamEvent(self, **params)` - Return next team Event for user
* `Teamcowboy.User_GetTeamEvents(self, **params)` - Return next team Events for user
* `Teamcowboy.User_GetTeamMessages(self, **params)` - Return team Messages for user
* `Teamcowboy.User_GetTeams(self, **params)` - Return users Teams
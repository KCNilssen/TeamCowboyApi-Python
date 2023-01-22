from typing import Dict, List
from .exceptions import TheTeamCowboyAPIException
import requests
import logging

from teamcowboyapi.objects.errors import Error


class TCResult:
    """
    A class that holds data, status_code, and message returned 
    from Team Cowboy api. http://api.teamcowboy.com/v1


    Attributes
    ----------
    status_code : int
        HTTP Return Code
    message : str
        Message returned from REST Endpoint
    data : dict
        JSON Data received from request
    """

    def __init__(self, status_code: int, message: str, data: Dict = {}):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data


class TCDataAdapter:
    """
    Adapter for calling the Team Cowboy endpoint

    Attributes
    ----------
    hostname : str
        rest endpoint for data
    ver : str
        api version
    logger : logging.Logger
        instance of logger class
    """

    

    def __init__(self, hostname: str = 'api.teamcowboy.com', ver: str = 'v1', logger: logging.Logger = None):
        self.url = f'https://{hostname}/{ver}/'
        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

    def post(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> TCResult:
        """
        return a TCResult from endpoint

        Parameters
        ----------
        endpoint : str
            rest api endpoint
        ep_params : dict
            params
        data : dict
            data to send with requests (we aren't using this)

        Returns
        -------
        TCResult
        """
        full_url = self.url + endpoint
        logline_pre = f'url={full_url}'
        logline_post = " ,".join((logline_pre, 'success={}, status_code={}, message={}, url={}'))

        try:
            self._logger.debug(logline_post)
            response = requests.post(url=full_url, data=data)

        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise TheTeamCowboyAPIException('Request failed') from e

        try:
            data = response.json()

        except (ValueError, requests.JSONDecodeError) as e: 
            self._logger.error(msg=(str(e)))
            raise TheTeamCowboyAPIException('Bad JSON in response') from e

        # Responce code is OK
        if response.status_code <= 200 and response.status_code <= 299:
            self._logger.debug(msg=logline_post.format('success',
            response.status_code, response.reason, response.url))

            if data['success'] == False:
                
                errorobject = Error(**data["body"])

                if errorobject.httpResponce >= 400 and errorobject.httpResponce <= 499:
                    self._logger.error(msg=logline_post.format(errorobject.errorCode,
                    errorobject.httpResponce, errorobject.message, response.url))

                    # return TCResult with 404 and empty data
                    return TCResult(errorobject.httpResponce, message=errorobject.message, data={})

                elif errorobject.httpResponce >= 500 and errorobject.httpResponce <= 599:
                    self._logger.error(msg=logline_post.format(errorobject.errorCode, 
                    errorobject.httpResponce, errorobject.message, response.url))

                    raise TheTeamCowboyAPIException(f"{errorobject.httpResponce}: {errorobject.message}")

                else:
                    raise TheTeamCowboyAPIException(f"{errorobject.httpResponce}: {errorobject.message}")
                
            else:
                # Everything is juicy, send the data over
                return TCResult(response.status_code, message=response.reason, data=data['body'])

        elif response.status_code >= 400 and response.status_code <= 499:  
            self._logger.error(msg=logline_post.format('Invalid Request',
            response.status_code, response.reason, response.url))

            # return MlbResult with 404 and empty data
            return TCResult(response.status_code, message=response.reason, data={})

        elif response.status_code >= 500 and response.status_code <= 599:

            self._logger.error(msg=logline_post.format('Internal error occurred', 
            response.status_code, response.reason, response.url))

            raise TheTeamCowboyAPIException(f"{response.status_code}: {response.reason}")

        else:
            raise TheTeamCowboyAPIException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, ep_params: Dict = None, data: Dict = None) -> TCResult:
        """
        return a TCResult from endpoint

        Parameters
        ----------
        endpoint : str
            rest api endpoint
        ep_params : dict
            params
        data : dict
            data to send with requests (we aren't using this)

        Returns
        -------
        TCResult
        """

        full_url = self.url + endpoint
        logline_pre = f'url={full_url}'
        logline_post = " ,".join((logline_pre, 'success={}, status_code={}, message={}, url={}'))

        try:
            self._logger.debug(logline_post)
            response = requests.get(url=full_url, params=ep_params)

        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise TheTeamCowboyAPIException('Request failed') from e

        try:
            data = response.json()

        except (ValueError, requests.JSONDecodeError) as e: 
            self._logger.error(msg=(str(e)))
            raise TheTeamCowboyAPIException('Bad JSON in response') from e

        # Responce code is OK
        if response.status_code <= 200 and response.status_code <= 299:
            self._logger.debug(msg=logline_post.format('success',
            response.status_code, response.reason, response.url))

            if data['success'] == False:
                
                errorobject = Error(**data["body"])

                if errorobject.httpResponce >= 400 and errorobject.httpResponce <= 499:
                    self._logger.error(msg=logline_post.format(errorobject.errorCode,
                    errorobject.httpResponce, errorobject.message, response.url))

                    # return TCResult with 404 and empty data
                    return TCResult(errorobject.httpResponce, message=errorobject.message, data={})

                elif errorobject.httpResponce >= 500 and errorobject.httpResponce <= 599:
                    self._logger.error(msg=logline_post.format(errorobject.errorCode, 
                    errorobject.httpResponce, errorobject.message, response.url))

                    raise TheTeamCowboyAPIException(f"{errorobject.httpResponce}: {errorobject.message}")

                else:
                    raise TheTeamCowboyAPIException(f"{errorobject.httpResponce}: {errorobject.message}")
                
            else:
                # Everything is juicy, send the data over
                return TCResult(response.status_code, message=response.reason, data=data['body'])

        elif response.status_code >= 400 and response.status_code <= 499:  
            self._logger.error(msg=logline_post.format('Invalid Request',
            response.status_code, response.reason, response.url))

            # return MlbResult with 404 and empty data
            return TCResult(response.status_code, message=response.reason, data={})

        elif response.status_code >= 500 and response.status_code <= 599:

            self._logger.error(msg=logline_post.format('Internal error occurred', 
            response.status_code, response.reason, response.url))

            raise TheTeamCowboyAPIException(f"{response.status_code}: {response.reason}")

        else:
            raise TheTeamCowboyAPIException(f"{response.status_code}: {response.reason}")

from dataclasses import dataclass

@dataclass
class Error:
    """
    If an API method is called and something goes wrong, you should receive an 
    error object (serialized as JSON or PHP) in the body of the response.
    
    Attributes:
    -----------
    errorCode : str
        The unique error code for the error. See below for a list of error 
        codes that may be returned from requests to the API.
    httpResponse : int
        The HTTP/1.1 status code that was returned. See HTTP/1.1 Status Codes.
    message : str
        A message describing the error in more detail.
    """
    errorCode: str
    httpResponse: int
    message: str
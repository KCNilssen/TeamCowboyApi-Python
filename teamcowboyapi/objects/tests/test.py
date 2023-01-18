from dataclasses import dataclass

@dataclass
class Tresponce:
    """
    This is a very basic testing object via a HTTP GET or via a HTTP POST.
    
    Attributes:
    -----------
    helloWorld : str
        A string message confirming you called this test method successfully. 
        If a value for “testParam” was provided, it will be output here as 
        well.
    """
    helloWorld: str
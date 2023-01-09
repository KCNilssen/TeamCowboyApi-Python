from dataclasses import dataclass

@dataclass
class League:
    """
    Simple object describing the league.

    Attributes:
    -----------
    leagueId : int  
        League Id
    name : str 
        League name
    city : str 
        City
    stateProvince : str 
        State/province
    postalCode : str 
        ZIP/Postal code
    countryIso2 : str 
        ISO 2-letter country code
    websiteUrl : str 
        Web site URL
    """
    leagueId: int
    name: str
    city: str
    stateProvince: str
    postalCode: str
    countryIso2: str
    websiteUrl: str
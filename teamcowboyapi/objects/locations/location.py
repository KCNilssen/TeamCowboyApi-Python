from typing import Union
from dataclasses import dataclass

@dataclass
class Surface:
    """
    Simple object describing the “surface” of the location.
    
    Attributes:
    -----------
    type : str 
        The surface type (grass, turf, dirt, etc)
    typeDisplay : str 
        Display value for the surface type
    showType : bool 
        True if it makes sense to show the surface type for the location (this 
        takes into consideration whether a type is defined, etc.)
    """
    type: str
    typeDisplay: str
    showType: bool

@dataclass
class Lights:
    """
    Simple object describing lighting for the location.
    
    Attributes:
    -----------
    lights : str 
        Value for the lights setting for the location (yes, no, unknown, or na)
    lightsDisplay : str 
        Display value for the lights setting for the location
    hasLights : bool 
        True if the location has lights
    """
    lights: str
    lightsDisplay: str
    hasLights: bool

@dataclass
class Address:
    """
    Simple object describing the address for the location.
    
    Attributes:
    -----------
    addressLine1 : str 
        First address line
    addressLine2 : str 
        Second address
    city : str 
        City
    stateProvince : str 
        State/province
    postalCode : str 
        Zip/Postal code
    partOfTown : str 
        Part of town (neighborhood, etc)
    displayMultiLine : str 
        Multi-line display for the address (lines separated by newlines)
    displaySingleLine : str S
        ingle-line display for the address
    googleMapsUrl : str 
        Google Maps URL for the address
    googleMapsDirectionsUrl : str 
        Google Maps “Get Directions” URL for the address
    """
    addressLine1: str
    addressLine2: str
    city: str
    stateProvince: str
    postalCode: str
    partOfTown: str
    displayMultiLine: str
    displaySingleLine: str
    googleMapsUrl: str
    googleMapsDirectionsUrl: str

@dataclass
class Location:
    """
    A location, typically associated with one or more events.

    Attributes:
    -----------
    locationId : int
        Location Id
    name : str
        Location name
    surface : Surface
        Simple object describing the “surface” of the location.
    lights : Lights
        Simple object describing lighting for the location.
    address : Address
        Simple object describing the address for the location.
    visibility : str
        The visibility for the location (public or private)
    visibilityDisplay : str
        The display value for visibility.
    comments : str
        Location comments.
    """ 
    locationId: int
    name: str
    surface: Union[Surface, dict]
    lights: Union[Lights, dict]
    address: Union[Address, dict]
    visibility: str
    visibilityDisplay: str
    comments: str
    
    def __post_init__(self):
        self.surface = Surface(**self.surface)
        self.lights = Lights(**self.lights)
        self.address = Address(**self.address)
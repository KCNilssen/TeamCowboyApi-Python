from typing import List, Union, Optional
from dataclasses import dataclass

@dataclass
class Color:
    """
    Colors in the color swatch, describing the color.
    
    Attributes:
    -----------
    name : str 
        The name of the color.
    hexCode : str 
        The HTML hex code for the color (e.g., #FFFFFF for white).
    """
    name: str
    hexCode: str

@dataclass
class Colorswatch:
    """
    A color swatch that contains one or more colors. Typically color swatches 
    are assigned to a team or opponent team for an event on a team's event 
    schedule.
    
    Attributes:
    -----------
    label : str
        The label/title of the color swatch as a whole.
    colorCount : int
        The number of colors in the color swatch
    colors : List[Color]
        An array of colors in the color swatch. Each array element is an 
        object describing the color.
    """
    colorCount: int
    colors: List[Union[Color, dict]]
    title: str
    label: Optional[str] = None
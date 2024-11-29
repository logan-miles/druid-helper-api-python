from typing import Dict, List
from pydantic import BaseModel

class Wildshape(BaseModel):
    name: str
    description: str
    hit_points: int
    armor_class: int
    challenge_rating: float
    strength: int
    dexterity: int
    constitution: int
    speed: Dict[str, int]
    environments: List[str]

class Wildshapes(BaseModel):
    wildshapes: List[Wildshape]
from typing import Dict, List
from pydantic import BaseModel

from druid_helper_api.wildshape.wildshape import Wildshape

class Monster(BaseModel):
    name: str
    description: str
    hit_points: int
    armor_class: int
    challenge_rating: float
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    speed: Dict[str, int]
    environments: List[str]
    type: str

    def to_wildshape(self) -> Wildshape:
        return Wildshape(**self.model_dump())

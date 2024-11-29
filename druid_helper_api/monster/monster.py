from typing import Dict, List
from pydantic import BaseModel

class Monster(BaseModel):
    name: str
    desc: str
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

class Monsters(BaseModel):
    monsters: List[Monster]
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
        wildshape: Wildshape = Wildshape(
            name = self.name,
            description = self.description,
            hit_points = self.hit_points,
            armor_class = self.armor_class,
            challenge_rating = self.challenge_rating,
            strength = self.strength,
            dexterity = self.dexterity,
            constitution = self.constitution,
            speed = self.speed,
            environments = self.environments
        )
        return wildshape

class Monsters(BaseModel):
    monsters: List[Monster]
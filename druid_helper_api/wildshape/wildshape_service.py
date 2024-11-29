from typing import Iterable, cast
from pydantic import BaseModel, PrivateAttr

from druid_helper_api.druid.druid import Druid
from druid_helper_api.monster.monster import Monster
from druid_helper_api.monster.monster_service import MonsterService
from druid_helper_api.wildshape.wildshape import Wildshape, Wildshapes

class WildshapeService(BaseModel):
    _monster_service: MonsterService = PrivateAttr()

    def __init__(self, monster_service: MonsterService):
        super().__init__()
        self._monster_service = monster_service

    def get_wildshapes(self, druid: Druid) -> Wildshapes:
        # TODO: Add actual functionality
        monsters = self._monster_service.get_monsters().monsters
        wildshapes = [m.to_wildshape() for m in cast(Iterable[Monster], monsters)]
        wildshapes_dict = {"wildshapes": wildshapes}
        wildshapes_actual = Wildshapes(**wildshapes_dict)
        
        return wildshapes_actual
        

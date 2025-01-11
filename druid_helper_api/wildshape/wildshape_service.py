from typing import List
from pydantic import BaseModel, PrivateAttr

from druid_helper_api.druid.druid import Druid
from druid_helper_api.monster.monster_repository import MonsterRepository
from druid_helper_api.wildshape.wildshape import Wildshape

class WildshapeService(BaseModel):
    _monster_service: MonsterRepository = PrivateAttr()

    def __init__(self, monster_service: MonsterRepository):
        super().__init__()
        self._monster_service = monster_service

    def get_wildshapes(self, druid: Druid) -> List[Wildshape]:
        # TODO: Add actual functionality

        return [m.to_wildshape() for m in self._monster_service.get_monsters()]
        
        
        

import json
from typing import List
from druid_helper_api.monster.monster import Monster, Monsters
from druid_helper_api.monster.monster_service import MonsterService
from pathlib import Path
from pydantic import BaseModel, Json, PrivateAttr, TypeAdapter


class MonsterServiceJson(MonsterService):
    _monsters: Monsters = PrivateAttr()

    def __init__(self, file: Path): 
        super().__init__()
        with file.open(encoding="UTF-8") as monster_file:
            loaded_file = json.load(monster_file)
        
            self._monsters = Monsters(**loaded_file)

    def get_monsters(self) -> Monsters:
        return self._monsters

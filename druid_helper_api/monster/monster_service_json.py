import json
from typing import List
from druid_helper_api.monster.monster import Monster
from druid_helper_api.monster.monster_service import MonsterService
from pathlib import Path
from pydantic import PrivateAttr, TypeAdapter


class MonsterServiceJson(MonsterService):
    _monsters: List[Monster] = PrivateAttr()

    def __init__(self, file: Path): 
        super().__init__()
        with file.open(encoding="UTF-8") as monster_file:
            loaded_file = json.load(monster_file)
        
            self._monsters = TypeAdapter(List[Monster]).validate_python(loaded_file)

    def get_monsters(self) -> List[Monster]:
        return self._monsters

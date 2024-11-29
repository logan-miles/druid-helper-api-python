from pathlib import Path
from typing import List
from druid_helper_api.monster.monster import Monster
from druid_helper_api.monster.monster_service_json import MonsterServiceJson


def test_init():
    file_path: Path = Path(__file__).parent.joinpath("local_monsters.json")
    monster_service = MonsterServiceJson(file_path)
    
    monsters: List[Monster] = monster_service.get_monsters()
    
    assert len([m for m in monsters if m.name == "walk-000"]) == 1
from pathlib import Path
from typing import Iterable, cast
from druid_helper_api.monster.monster import Monster, Monsters
from druid_helper_api.monster.monster_service_json import MonsterServiceJson


def test_init():
    file_path: Path = Path(__file__).parent.joinpath("local_monsters.json")
    monster_service = MonsterServiceJson(file_path)
    
    monsters: Monsters = monster_service.get_monsters()
    
    assert len([m for m in cast(Iterable[Monster], monsters.monsters) if m.name == "Walk 000"]) == 1
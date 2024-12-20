from pathlib import Path
from typing import List
from druid_helper_api.druid.druid import Druid
from druid_helper_api.monster.monster_service_json import MonsterServiceJson
from druid_helper_api.wildshape.wildshape import Wildshape
from druid_helper_api.wildshape.wildshape_service import WildshapeService


file_path: Path = Path(__file__).parent.parent.joinpath("monster/local_monsters.json")
monster_service = MonsterServiceJson(file_path)

wildshape_service = WildshapeService(monster_service = monster_service)

def test_init():
    walk_000: List[Wildshape] = [ws for ws in wildshape_service.get_wildshapes(Druid(level=1, subclass="moon")) if ws.name == "walk-000"]
    assert len(walk_000) == 1

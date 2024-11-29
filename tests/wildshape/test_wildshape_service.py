from pathlib import Path
from typing import Iterable, cast
from druid_helper_api.druid.druid import Druid
from druid_helper_api.monster.monster_service_json import MonsterServiceJson
from druid_helper_api.wildshape.wildshape import Wildshape, Wildshapes
from druid_helper_api.wildshape.wildshape_service import WildshapeService


file_path: Path = Path(__file__).parent.parent.joinpath("monster/local_monsters.json")
monster_service = MonsterServiceJson(file_path)

wildshape_service = WildshapeService(monster_service = monster_service)

def test_init():
    walk_000: Wildshapes = [ws for ws in cast(Iterable[Wildshape], wildshape_service.get_wildshapes(Druid()).wildshapes) if ws.name == "walk-000"]
    assert len(walk_000) == 1

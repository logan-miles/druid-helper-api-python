from pathlib import Path
from typing import List

import pytest
from druid_helper_api.druid.druid import Druid
from druid_helper_api.monster.monster_repository_json import MonsterRepositoryJson
from druid_helper_api.wildshape.wildshape import Wildshape
from druid_helper_api.wildshape.wildshape_service import WildshapeService


file_path: Path = Path("tests/monster/local_monsters.json")
monster_service = MonsterRepositoryJson(file_path)

wildshape_service = WildshapeService(monster_service=monster_service)


@pytest.mark.skip(reason="Functionality not implemented")
def test_no_wildshapes_at_level_1():
    wildshapes: List[Wildshape] = [
        ws for ws in wildshape_service.get_wildshapes(Druid(level=1))
    ]

    assert len(wildshapes) == 0


@pytest.mark.skip(reason="Functionality not implemented")
def test_one_wildshape_at_level_2():
    wildshapes: List[Wildshape] = [
        ws.name for ws in wildshape_service.get_wildshapes(Druid(level=2))
    ]

    assert len(wildshapes) == 2


@pytest.mark.skip(reason="Functionality not implemented")
def test_beasts_only():
    wildshapes: List[Wildshape] = [
        ws for ws in wildshape_service.get_wildshapes(Druid(level=20))
    ]
    monster_types = {m.name: m.type for m in monster_service.get_monsters()}

    assert all(monster_types[ws.name] == "Beast" for ws in wildshapes)


@pytest.mark.skip(reason="Functionality not implemented")
def test_speeds_under_4():
    wildshapes: List[Wildshape] = [
        ws for ws in wildshape_service.get_wildshapes(Druid(level=3))
    ]

    assert not any(("swim" in ws.speed or "fly" in ws.speed) for ws in wildshapes)
    assert any("walk" in ws.speed for ws in wildshapes)


@pytest.mark.skip(reason="Functionality not implemented")
def test_speeds_under_8():
    wildshapes: List[Wildshape] = [
        ws for ws in wildshape_service.get_wildshapes(Druid(level=7))
    ]

    assert not any("fly" in ws.speed for ws in wildshapes)
    assert any(("walk" in ws.speed and "swim" in ws.speed) for ws in wildshapes)


@pytest.mark.skip(reason="Functionality not implemented")
def test_speeds_8_or_over():
    wildshapes: List[Wildshape] = [
        ws for ws in wildshape_service.get_wildshapes(Druid(level=20))
    ]

    assert any(
        ("walk" in ws.speed and "swim" in ws.speed and "fly" in ws.speed)
        for ws in wildshapes
    )


non_moon_cr = [
    (2, 0.25),
    (3, 0.25),
    (4, 0.5),
    (5, 0.5),
    (6, 0.5),
    (7, 0.5),
    (8, 1),
    (9, 1),
    (10, 1),
    (11, 1),
    (12, 1),
    (13, 1),
    (14, 1),
    (15, 1),
    (16, 1),
    (17, 1),
    (18, 1),
    (19, 1),
    (20, 1),
]


@pytest.mark.skip(reason="Functionality not implemented")
@pytest.mark.parametrize("level, max_cr", non_moon_cr)
def test_max_cr_non_moon(level, max_cr):
    wildshape_crs: List[Wildshape] = [
        ws.challenge_rating
        for ws in wildshape_service.get_wildshapes(Druid(level=level))
    ]

    assert max(wildshape_crs) == max_cr


moon_cr = [
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 2),
    (7, 2),
    (8, 2),
    (9, 3),
    (10, 3),
    (11, 3),
    (12, 4),
    (13, 4),
    (14, 4),
    (15, 5),
    (16, 5),
    (17, 5),
    (18, 6),
    (19, 6),
    (20, 6),
]


@pytest.mark.skip(reason="Functionality not implemented")
@pytest.mark.parametrize("level, max_cr", moon_cr)
def test_max_cr_moon(level, max_cr):
    wildshape_crs: List[Wildshape] = [
        ws.challenge_rating
        for ws in wildshape_service.get_wildshapes(Druid(level=level, subclass="moon"))
    ]

    assert max(wildshape_crs) == max_cr

import json
from pathlib import Path
from typing import List
import pytest
from responses import matchers
import responses

from pydantic import TypeAdapter

from druid_helper_api.monster.monster import Monster
from druid_helper_api.monster.monster_repository_open5e import (
    MonsterRepositoryOpen5e,
    Open5eResponse,
)

file_path: Path = Path("tests/monster/resources/open5e_monsters_paged.json")

with file_path.open(encoding="UTF-8") as monster_file:
    loaded_file = json.load(monster_file)

monster_responses = TypeAdapter(List[Open5eResponse]).validate_python(loaded_file)


@responses.activate
def test_get_monsters_with_pages():
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[0].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[1].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10&page=2")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[2].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10&page=3")],
    )

    monster_service = MonsterRepositoryOpen5e(limit=10)
    monsters: List[Monster] = monster_service.get_monsters()
    assert len(monsters) == 30


@responses.activate
def test_get_monsters_with_pages_failure():
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[0].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        body=Exception(),
        status=500,
        match=[matchers.query_string_matcher("format=json&limit=10&page=2")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[2].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10&page=3")],
    )

    monster_service = MonsterRepositoryOpen5e(limit=10)
    monsters: List[Monster] = monster_service.get_monsters()
    assert len(monsters) == 20


@responses.activate
def test_get_monsters_with_pages_multiple_failures():
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[0].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        body=Exception(),
        status=500,
        match=[matchers.query_string_matcher("format=json&limit=10&page=2")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        body=Exception(),
        status=500,
        match=[matchers.query_string_matcher("format=json&limit=10&page=3")],
    )

    monster_service = MonsterRepositoryOpen5e(limit=10)
    monsters: List[Monster] = monster_service.get_monsters()
    assert len(monsters) == 10


@responses.activate
def test_get_monsters_first_page_failure():
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        body=Exception(),
        status=500,
        match=[matchers.query_string_matcher("format=json&limit=10")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[1].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10&page=2")],
    )
    responses.add(
        method=responses.GET,
        url="https://api.open5e.com/monsters/",
        json=monster_responses[2].model_dump(),
        status=200,
        match=[matchers.query_string_matcher("format=json&limit=10&page=3")],
    )

    monster_service = MonsterRepositoryOpen5e(limit=10)
    monsters: List[Monster] = monster_service.get_monsters()
    assert len(monsters) == 0


@pytest.mark.skip(reason="Manual only for testing real source")
def test_real():
    monster_service = MonsterRepositoryOpen5e(limit=100)
    monsters: List[Monster] = monster_service.get_monsters()
    assert len(monsters) > 1

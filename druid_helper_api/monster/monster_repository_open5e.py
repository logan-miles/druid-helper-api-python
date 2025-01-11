import re
from typing import Dict, List, Optional, OrderedDict
from urllib.parse import urlencode
from pydantic import BaseModel, PrivateAttr, computed_field
import requests

from druid_helper_api.monster.monster import Monster
from druid_helper_api.monster.monster_repository import MonsterRepository
from druid_helper_api.wildshape.wildshape import Wildshape


class Open5eMonster(BaseModel):
    name: str
    desc: str
    hit_points: int
    armor_class: int
    cr: float
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    speed: Dict[str, int]
    environments: List[str]
    type: str

    @computed_field
    def description(self) -> str:
        return self.desc

    @computed_field
    def challenge_rating(self) -> float:
        return self.cr

    def to_wildshape(self) -> Wildshape:
        return Wildshape(**self.model_dump())


class Open5eResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Open5eMonster]


class MonsterRepositoryOpen5e(MonsterRepository, BaseModel):
    _base_url: str = PrivateAttr()
    _params: OrderedDict = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__()
        self._params = OrderedDict(
            {"format": "json", "limit": kwargs.get("limit") or 100}
        )
        self._base_url = kwargs.get("base_url") or "https://api.open5e.com/monsters/"

    def get_monsters(self):
        monsters: List[Monster] = []
        params = self._params

        url = f"{self._base_url}?{urlencode(params)}"
        failcount = 0

        while url and failcount < 2:
            try:
                res = Open5eResponse(**requests.get(url).json())
                failcount = 0
                monsters.extend([Monster(**m.model_dump()) for m in res.results])
                url = res.next
            except Exception:
                failcount += 1
                url = re.sub(
                    r"page=(\d+)", lambda m: f"page={str(int(m.group(1)) + 1)}", url
                )

        return monsters

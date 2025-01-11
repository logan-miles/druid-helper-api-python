from abc import ABC, abstractmethod
from typing import List

from pydantic import BaseModel

from druid_helper_api.monster.monster import Monster


class MonsterRepository(ABC, BaseModel):
    @abstractmethod
    def get_monsters(self) -> List[Monster]:
        pass

from pydantic import BaseModel


class Druid(BaseModel):
    level: int
    subclass: str

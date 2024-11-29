from druid_helper_api.monster.monster import Monster
from druid_helper_api.wildshape.wildshape import Wildshape


def test_monster_to_wildshape():
    monster_json = '''{
      "name": "walk-000",
      "description": "Walk 0 CR",
      "hit_points": 10,
      "armor_class": 10,
      "challenge_rating": 0,
      "strength": 10,
      "dexterity": 10,
      "constitution": 10,
      "intelligence": 10,
      "wisdom": 10,
      "charisma": 10,
      "speed": {
        "walk": 30
      },
      "environments": [
        "Arctic",
        "Coast"
      ],
      "type": "Beast"
    }'''
    monster: Monster = Monster.model_validate_json(monster_json)

    wildshape: Wildshape = monster.to_wildshape()

    assert wildshape.name == monster.name
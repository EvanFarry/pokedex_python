from classes.pokemon import Pokemon

import json

user_input = "650"

p = Pokemon(user_input)
poke_id = p.get_pokemon_id()
name = p.get_pokemon_name()
types =  p.get_pokemon_types()
base = p.get_pokemon_base_exp()
ab = p.get_pokemon_abilities()
games = p.get_pokemon_game_presence()

for each in games:
    print each



if len(types) == 1:
    print poke_id, name, types[0]
elif len(types) == 2:
    print poke_id, name, types[0], types[1]

from classes.pokemon import Pokemon

import json

user_input = "1"

p = Pokemon(user_input)
poke_id = p.get_pokemon_id()
name = p.get_pokemon_name()
types =  p.get_pokemon_types()
base = p.get_pokemon_base_exp()


if len(types) == 1:
    print poke_id, name, types[0]
elif len(types) == 2:
    print poke_id, name, types[0], types[1]

import httplib      #import httplib library for Http connection/ get request
import json         #import json for json.loads() encoding

# Class to represent a Pokemon Object
class Pokemon:
#------------------------------------
# __init__ funciton
# summary:      create a Pokemon Object with a JSON object as an attribute
# parameter:    pokemon name OR pokemon ID
# returns:      N/a
#------------------------------------
    def __init__(self, name_or_id):
        conn = httplib.HTTPConnection("pokeapi.co")
        self.json_data = self.set_json(name_or_id, conn)

#------------------------------------
# set_json function - (only used at object initialization)
# summary:       makes GET request to API
# parameter:     pokemon name OR pokemon ID
# returns:       JSON DATA
#------------------------------------
    def set_json(self, name_or_id, conn):
        conn.request("GET", "/api/v2/pokemon/"+ name_or_id +"/")
        response = conn.getresponse()
        return json.loads(response.read())

#------------------------------------
# Public Class Methods
#   1. get_pokemon_name()
#   2. get_pokemon_id()
#   3. get_pokemon_types()
#------------------------------------

#------------------------------------
# returns:       pokemon name
#------------------------------------
    def get_pokemon_name(self):
        return self.json_data["name"]

#------------------------------------
# returns:       pokemon name
#------------------------------------
    def get_pokemon_id(self):
        return self.json_data["id"]

#------------------------------------
# summary:      get the pokemon type or types, store in array
# returns:      array of types
#------------------------------------
    def get_pokemon_types(self):
        types = []
        index = 0
        for slot in self.json_data["types"]:
            types.append(self.json_data["types"][index]["type"]["name"])
            index = index + 1
        return types

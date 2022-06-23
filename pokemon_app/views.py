from django.shortcuts import render
import random
import requests
import pprint

# Create your views here.
def index(request):
    return render(request, "pages/index.html")



def get_info(pokemon_dict):
    """
    Given a pokemon dictionary, return a dictionary with keys of name, types, and image.
    """
    # pp.pprint(pokemon)
    # print(pokemon['name'])
    # print(pokemon['types']) #list of type items
    # print(pokemon['sprites']['front_default']) #url of img
    #eg {'name': 'cacturne', 'types': ['grass', 'dark'],
    #  'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/332.png'}
    return {'name': pokemon_dict['name'], 
    'types': [dict_['type']['name'] for dict_ in pokemon_dict['types']],
    'image': pokemon_dict['sprites']['front_default']}

def pokemon(request):
    id = request.GET.get('id')

    if id is None:
        id = random.randint(1,898)
    else:
        id = int(id)

    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/")
    pokemon = pokemon.json()

    poke_dict = get_info(pokemon)

    available_pokemon = list(range(1,899))
    available_pokemon.remove(id)
    count = 0
    team = []
    while count < 5:
        new_id = random.choice(available_pokemon)
        new_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{new_id}/")
        new_poke_dict = get_info(new_pokemon.json())
        if set(new_poke_dict['types']) & set(poke_dict['types']): #check if any common element, so if not empty
            team.append(new_poke_dict)
            count +=1
        available_pokemon.remove(new_id)
    
    poke_dict['team'] = team
    # print(poke_dict)

    return render(request, 'pages/pokemon.html', poke_dict)






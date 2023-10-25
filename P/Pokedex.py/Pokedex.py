import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_pokemon_info(pokemon_data):
    if pokemon_data:
        print(f"Name: {pokemon_data['name']}")
        print(f"ID: {pokemon_data['id']}")
        print("Abilities:")
        for ability in pokemon_data['abilities']:
            print(f"- {ability['ability']['name']}")
        print("Types:")
        for pokemon_type in pokemon_data['types']:
            print(f"- {pokemon_type['type']['name']}")
    else:
        print("Pokemon not found.")

if __name__ == "__main__":
    while True:
        pokemon_name = input("Enter a Pokémon's name or 'exit' to quit: ")
        if pokemon_name.lower() == 'exit':
            break

        pokemon_data = get_pokemon_data(pokemon_name)
        display_pokemon_info(pokemon_data)

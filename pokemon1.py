import requests
def main():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100&offset=200')
    library = response.json()

    infoAboutPokemons = library['results']

    minName = infoAboutPokemons[0].get('name')
    maxName = infoAboutPokemons[0].get('name')

    for i in range(len(infoAboutPokemons)):
        name = infoAboutPokemons[i].get('name')
        if len(minName) > len(name):
            minName = name
        elif len(maxName) < len(name):
            maxName = name
    print("Самое короткое имя " + minName)
    print("Cамое длинное имя " + maxName)

main()

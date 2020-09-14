import requests
def main():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100&offset=200')
    library = response.json()

    structure = library['results']

    min = structure[0].get('name')
    max = structure[0].get('name')

    for i in range(len(structure)):
        if len(min) > len(structure[i].get('name')):
            min = structure[i].get('name')
        elif len(max) < len(structure[i].get('name')):
            max = structure[i].get('name')
    print("Самое короткое имя " + min)
    print("Cамое длинное имя " + max)



main()

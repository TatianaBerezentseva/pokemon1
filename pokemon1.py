import requests
def main():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100&offset=200')
    library = response.json()

    structure = library['results']

    min = structure[0].get('name')
    max = structure[0].get('name')

    for i in range(len(structure)):
        iteration = structure[i].get('name')
        if len(min) > iteration:
            min = iteration
        elif len(max) < iteration:
            max = iteration
    print("Самое короткое имя " + min)
    print("Cамое длинное имя " + max)



main()

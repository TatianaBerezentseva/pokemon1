import requests
def main():
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100&offset=200')
    print("Hello world")
    print(r)
main()

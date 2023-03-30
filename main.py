from classes.API import API

def printAbilities(data):
    print(type(data))
    for a in data:
        name = a["ability"]["name"]
        slot = a["slot"]
        is_hidden = a["is_hidden"]
        print(f"Name: {name}, Slot: {slot}, Hidden: {is_hidden}")



def main():
    api = API("https://pokeapi.co/api/v2")
    diggletData = api.getRequest("pokemon/50") ## digglet
    charizardData = api.getRequest("pokemon/charizard")
    
    charizardAbilities = charizardData['abilities']
    diggletAbilities = diggletData['abilities']
    #print(charizardAbilities)
    printAbilities(charizardAbilities)
    print("\n\n\n")
    printAbilities(diggletAbilities)


if __name__ == "__main__":
    main()
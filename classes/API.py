import requests as req

# https://pokeapi.co/api/v2
class API:
    def __init__(self, base_url) -> None:
        self.base_url = base_url


    def getRequest(self, resource, **params):
        url = f"{self.base_url}/{resource}"
        response = req.get(url, params=params)
        return response.json()
    

    def jsonToFile(self, res):
        pass



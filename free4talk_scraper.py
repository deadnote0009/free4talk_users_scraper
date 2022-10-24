import requests


class Scraper():
    url = "https://free4talk-sync.herokuapp.com/sync/get/free4talk/groups/?a=sync-get-free4talk-groups"
    
    def __init__(self):
        self.url = self.url
    
    def get_json_data(self):
        res =requests.post(self.url)
        res.encoding='utf-8-sig'
        return res.json()
    
    def __str__(self):
        return str(self.requ.status)       


request_object = Scraper()
data = request_object.get_json_data()
x = 0
for room in data["data"]:
    for clients in data["data"][room]["clients"] :
        for client in clients:
            x += 1
            print(client)
        print("##" * 10)
print(type(data))
print(x)
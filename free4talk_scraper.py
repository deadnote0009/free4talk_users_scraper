import requests


class JsonRequest():

    __url = "https://free4talk-sync.herokuapp.com/sync/get/free4talk/groups/?a=sync-get-free4talk-groups"
    
    status = None
    
    @classmethod
    def get_json_data(cls):
        res =requests.post(cls.__url)
        res.encoding='utf-8-sig'
        cls.status = res.status_code
        return res.json()
    
    @classmethod
    def __str__(cls):
        return cls.status       


class ParsedData():
    
    def __init__(self):
        self.__data = JsonRequest.get_json_data()
        self.status = JsonRequest.status
        self.num_users = 0
    
    def extract_data(self):
        for room in self.__data["data"]:
            for user in self.__data["data"][room]["clients"] :
                self.num_users += 1
                print(f'id: {user["id"]} name: {user["name"]} followers: {user["followers"]}')
    
    def __str__(self):     
        return F"{self.num_users}"

    

ob = ParsedData()
ob.extract_data()
print(ob)
print(ob.status)
print(JsonRequest.__str__())
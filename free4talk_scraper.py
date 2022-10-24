import requests

# the following code is for extracting data about users from free4talk


class JsonRequest:
    # this url return json data including all the user info that we need
    __url = "https://free4talk-sync.herokuapp.com/sync/get/free4talk/groups/?a=sync-get-free4talk-groups"

    status = None

    # to make the post requrst and return the data as json data that python can handel
    @classmethod
    def get_json_data(cls):
        res = requests.post(cls.__url)
        res.encoding = "utf-8-sig"
        cls.status = res.status_code
        return res.json()

    # just to prent the status of the request
    @classmethod
    def __str__(cls):
        return cls.status


# this class for parsing the data returned from JsonRequest class
class ParsedData:
    def __init__(self):
        self.__data = JsonRequest.get_json_data()
        self.status = JsonRequest.status
        self.num_users = 0

    # just print out the parsed data to the screen
    def extracting_data(self):
        try:
            for room in self.__data["data"]:
                for user in self.__data["data"][room]["clients"]:
                    self.num_users += 1
                    print(f'Name: {user["name"]}, ID: {user["id"]}, Followers: {user["followers"]}, Following:{user["following"]}, Friends:{user["friends"]}')

            return True
        except KeyError:
            return False

    def __str__(self):
        return f"{self.num_users}"


def controller():
    data = ParsedData()
    if data.status == 200:
        if data.extracting_data():
            return f"Number of users is {data.num_users}"
    return "False"


if __name__ == "__main__":
    print(controller())

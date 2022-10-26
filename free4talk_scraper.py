import requests
import csv

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
    def __init__(self, json_data):
        self.__data = json_data
        self.num_users = 0
        self._header = ["Name", "Id", "Followers", "following", "friends"]

    # return one row at a time in order to add it to the csv file
    def extracting_data(self):
        try:
            for room in self.__data["data"]:
                for user in self.__data["data"][room]["clients"]:
                    self.num_users += 1

                    # return one row at a time in order to add it to the csv file
                    yield [
                        user["name"],
                        user["id"],
                        user["followers"],
                        user["following"],
                        user["friends"],
                    ]

            return True

        except KeyError:
            return False

    def __str__(self):
        return f"{self.num_users}"


# save data into a csv file called data.csv
class SaveAsCsv:

    # init the object
    def __init__(self):
        self._json_data = JsonRequest.get_json_data()
        self._status = JsonRequest.status
        self.parser = ParsedData(self._json_data)

    def save(self):
        with open("data.csv", "w") as file:
            writer = csv.writer(file)

            # first write the header returned from parser._header
            writer.writerow(self.parser._header)

            # and then parser.extracting_data will yield a row at time so we can write into the csv
            # until stopiteration error raised
            for row in self.parser.extracting_data():
                writer.writerow(row)


if __name__ == "__main__":
    ob = SaveAsCsv()
    ob.save()

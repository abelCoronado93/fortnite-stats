import requests, yaml

with open("conf/api_conf.yaml", 'r') as stream:
    try:
        headers = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

modes = ["solo", "duo", "squad"]

class Fortnite:

    global headers, modes

    def __init__(self, username, platform):
        self.username = username
        self.platform = platform

    def get_stats(self):
        url = "https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats"
        data = { 'user_id' : self.get_uid(self.username), 'platform' : self.platform }
        r = requests.post(url, data=data, headers=headers)
        return r.json()

    @staticmethod
    def get_uid(username):
        url = "https://fortnite-public-api.theapinetwork.com/prod09/users/id"
        data = { 'username' : username }
        r = requests.post(url, data=data, headers=headers)
        return r.json()["uid"]
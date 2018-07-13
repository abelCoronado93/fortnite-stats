import requests, yaml, pry

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
        r = self.get_uid(self.username)

        data = { 'user_id' : r["uid"], 'platform' : self.platform }
        return requests.post(url, data=data, headers=headers).json()

    @staticmethod
    def get_uid(username):
        url = "https://fortnite-public-api.theapinetwork.com/prod09/users/id"
        data = { 'username' : username }
        r = requests.post(url, data=data, headers=headers).json()
        if 'uid' in r:
            return r
        else:
            raise InvalidUsage('User not found', status_code=400)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
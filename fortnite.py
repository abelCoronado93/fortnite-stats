import requests
import sys

headers = { "Authorization" : "MyAPIKey" }
username = sys.argv[1]
platform = sys.argv[2]
modes = ["solo", "duo", "squad"]

def get_uid():
    url = "https://fortnite-public-api.theapinetwork.com/prod09/users/id"
    data = { 'username' : username }
    r = requests.post(url, data=data, headers=headers)
    return r.json()["uid"]

def print_mode(user_stats, mode):
    print()
    print("############# " + mode.upper() + " #############")
    print("Kills: %i" % user_stats["stats"]["kills_" + mode])
    print("Wins: %i" %user_stats["stats"]["placetop1_" + mode])
    print("Matches played: %i" %user_stats["stats"]["matchesplayed_" + mode])
    print("Kill rate: %.2f" %user_stats["stats"]["kd_" + mode])
    print("Win rate: %.2f" %user_stats["stats"]["winrate_" + mode])

def print_totals(user_stats):
    print()
    print("############# TOTALS #############")
    print("Kills: %i" % user_stats["totals"]["kills"])
    print("Wins: %i" %user_stats["totals"]["wins"])
    print("Matches played: %i" %user_stats["totals"]["matchesplayed"])
    print("Hours played: %i" %user_stats["totals"]["hoursplayed"])
    print("Kill rate: %.2f" %user_stats["totals"]["kd"])
    print("Win rate: %.2f" %user_stats["totals"]["winrate"])

url = "https://fortnite-public-api.theapinetwork.com/prod09/users/public/br_stats"
data = { 'user_id' : get_uid(), 'platform' : platform }

r = requests.post(url, data=data, headers=headers)
user_stats = r.json()

for mode in modes:
    print_mode(user_stats, mode)

print_totals(user_stats)
# Flask App with Docker
Web app to know your Fortnite stats.

## Requisites
 - Docker
 - Fortnite API Key (https://fortniteapi.com) [Requests limit per 24 hours is 250]
 - Replace "MyAPIKey" in the yaml
 
## Installation

```
 docker build -t <image_name> .
 docker run --name fortnite-stats -p 80:5000 <image_name>
```
 - Browser: http:/localhost:80


# fortnite-stats script (.sh)
Python script to know your Fortnite stats.

## Requisites

- Python
- Fortnite API Key (https://fortniteapi.com) [Requests limit per 24 hours is 250]
- Replace "MyAPIKey" in the script `fortnite.py`

## Use

```
python fortnite.py <username> <platform>
```
Platforms: `pc, xb1 or ps4`

## Example

```
python fortnite.py Ninja pc
```

Output

```
############# SOLO #############
Kills: 29172
Wins: 1332
Matches played: 3772
Kill rate: 11.96
Win rate: 35.31

############# DUO #############
Kills: 21935
Wins: 1306
Matches played: 3014
Kill rate: 12.84
Win rate: 43.33

############# SQUAD #############
Kills: 15891
Wins: 691
Matches played: 2382
Kill rate: 9.40
Win rate: 29.01

############# TOTALS #############
Kills: 66998
Wins: 3329
Matches played: 9168
Hours played: 835
Kill rate: 11.47
Win rate: 36.31
```

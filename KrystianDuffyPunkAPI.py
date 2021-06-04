#By Krystian Duffy
import requests
import json

#function used to group the beers by yeast
def sortFunc(beer):
	return beer["ingredients"]["yeast"]

#processes user input with checks for validity
while True:
    lowBound = input("Enter an ABV lower bound: ")
    upBound = input("Enter an ABV upper bound: ")
    valid = True
    try:
        lowBound = int(lowBound)
        upBound = int(upBound)
    except:
        valid = False
        print("Invalid Input \n\r")
    if(upBound > lowBound and valid):
        break
    elif(upBound < lowBound):
        print("upper Bound must be greater than lower bound \n\r")

#gets API data using upper and lower ABV bounds
request = "https://api.punkapi.com/v2/beers?abv_gt=" + str(lowBound) + "&abv_lt=" + str(upBound)
response = requests.get(request)

#loads the data as json and sorts it by yeast
beers = json.loads(response.text)
beers = sorted(beers, key=sortFunc)

#iterates through the list of beers displaying their data
for beer in beers:
    print("Name: " + beer["name"])
    print("     Image Url: " + beer["image_url"])
    print("     Description: " + beer["description"])
    print("     Tagline: " + beer["tagline"])

    hops = beer["ingredients"]["hops"]
    hopsList = [""]*len(hops)
    index = 0
    for hop in hops:
        hopsList[index] = hop["name"]
        index += 1

    index = 0
    malts = beer["ingredients"]["malt"]
    maltsList = [""]*len(malts)
    for malt in malts:
        maltsList[index] += malt["name"]
        index += 1

    print("     Hops: " + ", ".join(hopsList))
    print("     Malts: " + ", ".join(maltsList))

    print("")
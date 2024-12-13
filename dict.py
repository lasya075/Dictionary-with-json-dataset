import json
data = json.load(open("data.json"))
from difflib import get_close_matches
def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        print("did u mean %s instead" %get_close_matches(word,data.keys())[0])
        decide = input( "y or n")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return("u pressed on wrong keys")
        else:
            return("you have entered wrong input press y or n")
    else:
        print("please check again")

x = input("enter the word")
y = x.lower()
output = translate(y)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

import requests
import json

apiUrl = "https://api.datamuse.com/words?rel_jjb=ocean"

response = requests.get(apiUrl)
jsonData = response.json()

prettyPrint = json.dumps(jsonData, indent=4)

with open("prettyOutput.json", "w") as jsonFile:
    jsonFile.write(prettyPrint)

print(prettyPrint)

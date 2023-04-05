import json

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
print(ourjson)
print("El Token de acceso es: {}".format(ourjson['access_token']))
print("El Token expira en {} segundos.".format(ourjson['expires_in']))


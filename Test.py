import requests

API_link = "https://api.telegram.org/bot990300710:AAFlnOa2JvGaqCQaY2BsP8GZW3Id4fGMD5k"

updates = requests.get(API_link + "/getUpdates").json

print(updates)
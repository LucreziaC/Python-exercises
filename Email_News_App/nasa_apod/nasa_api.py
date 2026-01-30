import requests
from pathlib import Path

API_KEY = "hX6Y3NGgNTBwM01gAWKh6jmd8GlQxXXUp9Wjoz4r"
BASE_DIR = Path(__file__).resolve().parent
url = "https://api.nasa.gov/planetary/apod"

def download_image(url):
    image= requests.get(url).content
    with open("image.jpg", "wb") as handler:
        handler.write(image)
        

def get_apod():
    request = requests.get(f"{url}?api_key={API_KEY}")
    content = request.json()
    apod = {
        "title": content["title"],
        "image": content['url'],
        "copyright": content['copyright'],
        "description": content['explanation']
    }
    return apod

def download_image(url, path):
    image= requests.get(url).content
    with open(path, "wb") as handler:
        handler.write(image)
    return path


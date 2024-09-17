import urllib.request

# from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg"

with urllib.request.urlopen(url) as url:
    print(url.read())


# img = Image.open("temp.jpg")
# img.show()

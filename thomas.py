import ssl
import urllib.request

from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg"
tmp = "tmpfile.jpg"
context = ssl._create_unverified_context()
urllib.request.urlretrieve(url, tmp, context)
Image.open(tmp).show()

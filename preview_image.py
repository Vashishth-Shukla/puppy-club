import urllib.request

from PIL import Image


def preview_image(url):
    tmp = "tmpfile.jpg"
    urllib.request.urlretrieve(url, tmp)
    Image.open(tmp).show()


def main():
    url = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bulldog_inglese.jpg"
    preview_image(url)


if __name__ == "__main__":
    main()

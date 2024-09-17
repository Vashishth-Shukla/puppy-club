import wikipedia


def url_and_description(dog_breed):
    summary = wikipedia.summary(dog_breed, sentences=2)
    page = wikipedia.page(dog_breed)
    image_url = page.images[2] if page.images else None
    return image_url, summary


### sanety check!
def main():
    breed = "Bulldog"
    img_url, summary = url_and_description(breed)
    print("url: ", img_url)
    print("summary: ", summary)


if __name__ == "__main__":
    main()

import wikipedia


def url_and_description(dog_breed):
    """
    Get photo-url and the summery for the wikipedia.

    Args:
        dog_breed (str) : the name of the breed

    Returns:
        (image_url (str), summary (str)) : (the link to the photo of a dog of that breed, A short description of the breed)

    """
    summary = wikipedia.summary(dog_breed, sentences=2, auto_suggest=False)
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

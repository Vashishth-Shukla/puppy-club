DOG_BREEDS = [
    "Dobermann",
    "Bulldog",
    "American Staffordshire Terrier",
    "Irish Wolfhound",
    # "Bullterrier",
    "Jack Russell Terrier",
    # "Dachshund",
    "Rottweiler",
    "Greyhound",
    # "Labrador Retriever",
    "Kangal Shepherd",
]


### test
def main():
    from url_and_description import url_and_description

    for breed in DOG_BREEDS:
        _, summary = url_and_description(breed)
        summary = summary.replace(breed, "'funny little puddle'")
        print()
        print(breed + ": ")
        print(summary)


if __name__ == "__main__":
    main()

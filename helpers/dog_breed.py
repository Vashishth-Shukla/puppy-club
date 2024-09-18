import wikipedia

# Set the language to English (default) or change to German if desired
wikipedia.set_lang("en")

DOG_BREEDS = [
    "German Shepard",
    "Labrador Retriever",
    "Greyhound",
    "Cocker Spaniels",
    "Border Collie",
    "Rottweiler",
    # "St. Bernard",
    "Siberian Husky",
    "Jack Russell Terrier",
    "Dobermann",
    "Bull Terrier",
    "American Staffordshire Terrier",
    "French Bulldog",
    "Kangal Shepherd Dog",
    "Arabian Greyhound",
    "Irish Wolfhound",
    "Bulldog",
    "Jack Russell Terrier",
    "Dalmatian dog",
    "Cane Corso",
    "Shiba Inu",
]
dog_breed = "St. Bernard"


# -David ... Thank you
def fetch_bread_character_wiki(dog_breed):
    ### function fetches the summary of a given dog breed by using the wiki module. function receives a string and returns a string after fetching ###
    try:
        summary = wikipedia.summary(dog_breed, auto_suggest=False)
        return summary
    # Errors are non python errors and are specifically designed for    #the Wiki API
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation Error: {e.options}"
    except wikipedia.exceptions.PageError:
        return f"Page Error: {dog_breed} not found."


print(fetch_bread_character_wiki(dog_breed))
# for breed in DOG_BREEDS:
#     print(fetch_bread_character_wiki(breed))

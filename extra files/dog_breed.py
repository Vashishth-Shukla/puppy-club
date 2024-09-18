import wikipedia

# Set the language to English (default) or change to German if desired


# -David ... Thank you
def fetch_bread_character_wiki(dog_breed):
    wikipedia.set_lang("en")
    ### function fetches the summary of a given dog breed by using the wiki module. function receives a string and returns a string after fetching ###
    try:
        summary = wikipedia.summary(dog_breed, auto_suggest=False)
        return summary
    # Errors are non python errors and are specifically designed for    #the Wiki API
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation Error: {e.options}"
    except wikipedia.exceptions.PageError:
        return f"Page Error: {dog_breed} not found."


def main():
    test_breed = "Bulldog"
    print(fetch_bread_character_wiki(test_breed))


if __name__ == "__main__":
    main()

# for breed in DOG_BREEDS:
#     print(fetch_bread_character_wiki(breed))

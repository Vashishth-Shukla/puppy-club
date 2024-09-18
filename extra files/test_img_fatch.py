import wikipedia

from preview_image import preview_image
from url_and_description import url_and_description

DOG_BREEDS = [
    "Dobermann",
    "Bulldog",
    "American Staffordshire Terrier",
    "Irish Wolfhound",
    "Bullterrier",
    "Jack Russell Terrier",
    # "Chihuahua (dog breed)",
    # "Boxer (dog breed)",
    "Dachshund",
    "Rottweiler",
    "Greyhound",
    "Labrador Retriever",
    "Kangal Shepherd",
]


test_breed = ["Dachshund"]  #  DOG_BREEDS  #  ["Siberian Husky"]

for breed in test_breed:
    try:
        url, summary = url_and_description(breed)
        print("url: " + url)
        print("descritpion: " + summary)
        preview_image(url)

    except:
        print(f"bad breed : {breed}")
        # bad_breed.append(breed)

# result = list(set(breed_list) - set(bad_breed))
# print(result)

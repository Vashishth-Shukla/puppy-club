from preview_image import preview_image
from url_and_description import url_and_description

breed_list = [
    "German Shepherd",
    "Labrador Retriever",
    "Greyhound",
    "Cocker Spaniel",
    "Border Collie",
    "Rottweiler",
    "St.Bernard",
    "Siberian Husky",
    "Jack Russell Terrier",
    "Dobermann",
    "Bullterrier",
    "American Staffordshire Terrier",
    "French Bulldog",
    "Kangal Shepherd",
    "Arabian Greyhound",
    "Irish Wolfhound",
    "Bulldog",
    "Jack Russell Terrier",
    "Dalmatian",
    "Cane Corso",
    "Shiba Inu",
]

bad_breed = []
test_breed = ["St.Bernard"]
for breed in test_breed:
    try:
        url, summary = url_and_description(breed)
        preview_image(url)

    except:
        print(f"bad breed : {breed}")
        bad_breed.append(breed)

# result = list(set(breed_list) - set(bad_breed))
# print(result)

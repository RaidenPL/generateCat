import random
import requests

def names():
    # Set the API key
    api_key = "live_tD5qkwJFwDnWISvsWxPSB6Tij8Bz96jPdwktmOCzjBGUNKdKLls6XgKCiINJRLoc"
    
    # Make the API request
    response = requests.get("https://api.thecatapi.com/v1/breeds", headers={"x-api-key": api_key})
    
    # Check the status code of the response
    if response.status_code != 200:
        raise Exception("Failed to get cat breed names")
    
    # Extract the list of cat breed names from the response
    cat_breeds = response.json()
    names = [breed["name"] for breed in cat_breeds]

    random.shuffle(names)

    text = "\n".join(names)

    with open("./breedNames.txt", "w") as f:
        # Write the list of names to the file
        f.writelines(text)

    return
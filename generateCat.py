import requests
import nameOfCat as nameOfCat
from urllib.request import urlretrieve
from PIL import Image

def generateCat(prompt,filename):
    # Define the API endpoint and the headers for the request
    endpoint = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    
    # Define the payload for the request
    data = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "1024x1024",
        "response_format": "url"
    }
    
    # Make the POST request to the OpenAI API
    response = requests.post(endpoint, headers=headers, json=data)
    
    # Check the status code of the response
    if response.status_code != 200:
        raise Exception("Failed to generate image: {}".format(response.text))
    
    # Get the URL of the generated image from the response
    image_url = response.json()["data"][0]["url"]
    
    urlretrieve(image_url, filename)
    
    image = Image.open(filename)

    image.save(filename, "JPEG")

generateCat(nameOfCat.nameOfCat(),"cat.jpg")

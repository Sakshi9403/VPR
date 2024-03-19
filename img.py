import re
import os
import requests
from urllib.parse import urlparse

#name of the product
product_name = "Fostelo Shoulder bags"
input_text_file="Fostelo2.txt"

# Specify the path to the input file containing the fetch responses
input_file_path = r"C:\Users\HP\Desktop\git\Flikart-Image-scraper-main\fetch_Texts\{}".format(input_text_file)

# Specify the path to the output folder for saving the images
output_folder = r"C:\Users\HP\Desktop\git\Flikart-Image-scraper-main\images\{}".format(product_name)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read the content from the input file
with open(input_file_path, "r") as input_file:
    fetch_responses = input_file.readlines()

# Define a regular expression pattern to extract URLs of the first kind
url_pattern = r'https://rukminim1\.flixcart\.com/[^"\s]+'

# Initialize a counter for naming the downloaded images
image_counter = 1



# Download and save images from the extracted URLs
for fetch_response in fetch_responses:
    url_matches = re.findall(url_pattern, fetch_response)
    for url in url_matches:
        response = requests.get(url)
        if response.status_code == 200:
            # Extract the filename from the URL
            url_path = urlparse(url).path
            filename = os.path.basename(url_path)
            
            # Generate the image name
            image_name = f"{product_name}-{image_counter}.jpg"
            
            # Save the image to the output folder
            image_path = os.path.join(output_folder, image_name)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
            
            print(f"Downloaded {filename} as {image_name} to {image_path}")
            
            image_counter += 1
        else:
            print(f"Failed to download {url}")

print("Images downloaded and saved to", output_folder)

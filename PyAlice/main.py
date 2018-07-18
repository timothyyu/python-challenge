# Import text file with multiple paragraphs of text

# Retrive file remotely and store in raw_data folder
	# From Project Gutenberg:
		# Alice’s Adventures in Wonderland, Lewis Carroll
	# https://www.gutenberg.org/files/11/11-0.txt

# Approximate word count
# Approximate sentence count
# Approximate letter count per word
# Average sentence length in words

# Vader sentiment analysis
# ML/DNN Text structure analysis and generation of new text 
# D3/Dashboard visualizations

# Imports
import requests
from requests import get

# Download file from resource, store in raw_data
def download(url,file_name):
	with open(file_name, "wb") as file:
		# GET method stored as response variable
		response = get(url)
		print("URL/resource to be retrived:")
		print(url)
		print("Response from server for GET resquest: ")
		print(response)
		# read response as bytes and write to file
		print("Writing response to file...")
		file.write(response.content)
		print("Write complete.")

download("https://www.gutenberg.org/files/11/11-0.txt","raw_data/alice.txt")
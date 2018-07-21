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

import requests
import io

def download(url,file_name):
    with open(file_name, "wb") as file:
        response= requests.get(url)
        print("Response from server for GET request: ")
        print(response)
        print (response.text)
        file.write(response.content)
download("https://www.gutenberg.org/files/11/11-0.txt","alice.txt")
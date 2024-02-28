"""4.Create a program that attempts to connect to a website and prints the HTML content if successful. 
Use a try-except-else block to handle the requests.exceptions.RequestException exception and display an error message if the connection fails."""


import requests

def connect_to_website(url):

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception
    print(response.text)  # Access the HTML content as text
  except requests.exceptions.RequestException as error:
    print(f"Error: Failed to connect to website. Reason: {error}")
  else:
    print("Connection successful!")


url = "https://www.google.com" 
connect_to_website(url)



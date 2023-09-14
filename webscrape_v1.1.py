# webscrape_v1.1.py
# extremely simple web scraping using just the Python requests file.

# requests is a simple python library for making web requests
# you can find the documentation for it here:
# https://requests.readthedocs.io/en/latest/
import requests


# basically, all we're doing here is defining a URL, then just making
# a web request to the address
# unfortunately, this is really only effective for static webpages,
# for JS, we'll need to get a little crafty...
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# dump the page contents into the terminal
print(page.text)

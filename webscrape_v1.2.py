# webscrape_v1.2py
# extremely simple web scraping using just the Python requests file.
# now with soup!

# requests is a simple python library for making web requests
# you can find the documentation for it here:
# https://requests.readthedocs.io/en/latest/
import requests

# we're going to use Beautiful Soup 4, a simple html formatter for python
# notice how we're aliased it as "soupy", so we don't have to write out the word
# you can find the documentation for it here:
# https://pypi.org/project/beautifulsoup4/
from bs4 import BeautifulSoup as soupy

# basically, all we're doing here is defining a URL, then just making
# a web request to the address
# unfortunately, this is really only effective for static webpages,
# for JS, we'll need to get a little crafty...
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# dump the page contents into the terminal
# but this time, use the beautiful soup parser
# this parser is rather slow, however
# could there be additional parsers?
soup = soupy(page.content, "html.parser")
print(soup)


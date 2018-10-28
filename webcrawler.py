import bs4
import requests
import re
from tqdm import tqdm


def scrape_links(from_url, depth, urls = {}):
    """
    Scrapes links of a tags with links, is recursive, and "dives" as many times as the depth is set
    (Is very Exponential)
    """

    if depth >= 0:
        try :
            # if the request takes more than 3 sek (download link) terminate
            r = requests.get(from_url, timeout=3)
            # Throw error if code is not in 200's
            r.raise_for_status()
            # Create "soup"
            soup = bs4.BeautifulSoup(r.text, 'html5lib')

            # Find all a tags, and get only the ones starting with http and not ending with .vsix (special edge case with corrupt file)
            urls[from_url] = [link.get('href') for link in soup.find_all('a', attrs={'href': re.compile("^http.*(?<!.vsix)$")})]

            ## Start recursion             
            for url in tqdm(urls[from_url]):
                # Check if the url already has been scraped
                if url not in urls.keys(): 
                    urls = scrape_links(url, depth-1, urls)
        except :
            # if url is broken just move along
            pass
    return urls
    
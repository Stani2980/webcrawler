import sys
import os
import json
from webcrawler import scrape_links
from visualization import create_graph
"""
To run `python main.py <url> <depth>`
"""

START_URL = sys.argv[1]
DEPTH = int(sys.argv[2])
FILE_NAME = "links.py"

if __name__ == '__main__':
    res = scrape_links(START_URL, DEPTH)
    print(f'SCRAPED: {len(res)} links')

    ## Remove previous version of file, then create new python module
    try :
        os.remove(FILE_NAME)
    except:
        pass

    with open(FILE_NAME, 'w') as f:
        json.dump(res, f, indent=4)
    
    create_graph(res)
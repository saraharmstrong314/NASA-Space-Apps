import pandas as pd
import requests
from bs4 import BeautifulSoup

# no point matching planet type to duplicate exoplanet names
def getUniqueNames():
    df = pd.read_csv('exoplanet_names.csv')
    unique_names = df['pl_name'].unique()
    lst = unique_names.tolist()
    print(len(unique_names))
    with open('unique_names.txt', 'w') as f:
        for name in lst:
            f.write(name)
            f.write('\n')

if __name__ == "__main__":
    getUniqueNames()
    # imbalanced classes, use duplicate entries?
    # add short name to url, then repeat to get planet types
    url = 'https://example.com'
    headers = {
    'User-Agent': 'ScraperToGetExoplanetFullNamesBecauseExoplanetArchiveOnlyHasShortNames (ghlasphyre@gmail.com)'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
    else:
        print(f'Error: {response.status_code}')

    soup = BeautifulSoup(html_content, 'html.parser')
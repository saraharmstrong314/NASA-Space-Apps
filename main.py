import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# no point matching planet type to duplicate exoplanet names
def getUniqueNames():
    df = pd.read_csv('exoplanet_names.csv')
    unique_names = df['pl_name'].unique()
    unique_names_list = unique_names.tolist()
    
    return unique_names_list

# need full names to access urls to webscrape planet types
def getFullNames():
    short_names_list = getUniqueNames()
    service = Service(r'C:\Users\Flowe\MY_FILES\Projects\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    with open('full_names.txt', 'w') as f:
        for short_name in short_names_list:
            name = short_name.replace(' ', '_')
            url = f'https://eyes.nasa.gov/apps/exo/#/planet/{name}'
            driver.get(url)
            time.sleep(2)
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "entryTitleId")))
            except:
                f.write('ERROR')
                continue
            full_name = element.text
            f.write(f'{full_name}\n')
    driver.quit()
    print('done')

if __name__ == "__main__":
    getFullNames()
    # imbalanced classes, use duplicate entries?
    # add short name to url, then repeat to get planet types

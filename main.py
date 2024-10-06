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

# gets full names and planet types of exoplanets
def scrapeFullNamesAndPlanetTypes():
    short_names_list = getUniqueNames()
    service = Service(r'C:\Users\Flowe\MY_FILES\Projects\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    with open('full_names.txt', 'w') as f_names, open('planet_types.txt', 'w') as f_types:
        for short_name in short_names_list:
            name = short_name.replace(' ', '_')
            url = f'https://eyes.nasa.gov/apps/exo/#/planet/{name}'
            driver.get(url)
            # wait for page to load, else it's fickle with duplicating and skipping some names
            time.sleep(2)
            try:
                name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "entryTitleId")))
                planet_type_element = driver.find_element(By.XPATH, '//div[@id="footerBarId"]/button[1]')
            except:
                f_names.write('ERROR\n')
                f_types.write('ERROR\n')
                continue
            full_name = name_element.text
            planet_type = planet_type_element.text
            f_names.write(f'{full_name}\n')
            f_types.write(f'{planet_type}\n')
    driver.quit()

def cleanPlanetTypes(filename='planet_types.txt'):
    planet_list = []
    with open(filename, 'r') as f:
        planets = f.readlines()
        for planet in planets:
            planet_list.append(planet.strip('\n'))
    df = pd.DataFrame({'planet': planet_list})
    print(df['planet'].value_counts())


if __name__ == "__main__":
    cleanPlanetTypes()
    # imbalanced classes, use duplicate entries?
    # add short name to url, then repeat to get planet types

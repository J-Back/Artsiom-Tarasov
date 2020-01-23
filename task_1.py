import requests
import pandas as pd

COUNTY = ['Washington County, Rhode Island', 'Kent County, Rhode Island', 'Providence County, Rhode Island', 'Bristol County, Rhode Island',
          'Newport County, Rhode Island']
GEO_ = []
POPULATION_ = []
AGE_ = []
BUSINESS_ = []

def main():
    for COUNTY_NAME in COUNTY:
        GEO_.append(requests.get("https://factfinder.census.gov/rest/communityFactsNav/nav?", params = {'searchTerm': COUNTY_NAME, 'spotlightId': 'ALL'}).json()['CFMetaData']['geo'])
        POPULATION_.append(requests.get("https://factfinder.census.gov/rest/communityFactsNav/nav?", params = {'searchTerm': COUNTY_NAME, 'spotlightId': 'ALL'}).json()['CFMetaData']['measuresAndLinks']['allMeasures'][0]['list'][1]['value'])
        AGE_.append(requests.get("https://factfinder.census.gov/rest/communityFactsNav/nav?", params = {'searchTerm': COUNTY_NAME, 'spotlightId': 'ALL'}).json()['CFMetaData']['measuresAndLinks']['allMeasures'][1]['value'])
        BUSINESS_.append(requests.get("https://factfinder.census.gov/rest/communityFactsNav/nav?", params = {'searchTerm': COUNTY_NAME, 'spotlightId': 'ALL'}).json()['CFMetaData']['measuresAndLinks']['allMeasures'][2]['value'])

    data = pd.DataFrame({
        'GEO': GEO_,
        'POPULATION': POPULATION_,
        'AGE': AGE_,
        'BUSINESS': BUSINESS_,
    })

    print(data)
    data.to_csv('file.csv')

if __name__ == '__main__':
    main()

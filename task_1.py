import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Cookie': 's_fid=4B1434BDA822F6E7-0C0CFB5F80EE20FA; s_gnr=1579718150380-Repeat; s_vnum=1584880851313%26vn%3D3; JSESSIONID=0001kFNNmen4W2KakexnjjjnDb3:182lpgsca; RDS_DADS_PERSIST=!2mxabrZr7+RycExKYWF0Em1V6nI2hzG0QjVxSGD/c5Os+tZVJfT2s0p/X33GEDH8varVxNjQpoP+or4=; TS01fa88a5=011ba694f2594ccfaefea451e549a9da40d176c55b51e69531f74d196d1185254fbe4b78e94fe47b04bb0113d5fbfa0a032bf9cd19; undefined_s=First%20Visit; s_invisit=true; s_cc=true',
    'Host': 'factfinder.census.gov',
    'Referer': 'https://factfinder.census.gov/faces/nav/jsf/pages/community_facts.xhtml',
    'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

data_population = {
    'N': 0,
    '_t': 1579719916529,
    'log': 't',
    'measureId': 'PEP_EST',
    'spotlightId': 'POPULATION'
}

data_age = {
    'N': 0,
    '_t': 1579718949415,
    'log': 't',
    'spotlightId': 'AGE'
}

data_business = {
    'N': 0,
    '_t': 1579719112431,
    'log': 't',
    'spotlightId': 'BUSINESS_AND_INDUSTRY'
}

def main():
    response_population = requests.post("https://factfinder.census.gov/rest/communityFactsNav/nav", headers = headers, data = data_population)
    response_age = requests.post("https://factfinder.census.gov/rest/communityFactsNav/nav", headers = headers, data = data_age)
    response_business = requests.post("https://factfinder.census.gov/rest/communityFactsNav/nav", headers = headers, data = data_business)

    population_json = response_population.json()
    age_json = response_age.json()
    business_json = response_business.json()

    geo = population_json['CFMetaData']['geo']
    population = population_json['CFMetaData']['measuresAndLinks']['measure']['value']
    age = age_json['CFMetaData']['measuresAndLinks']['measure']['value']
    business = business_json['CFMetaData']['measuresAndLinks']['measure']['value']
    
    print(geo)
    print(population)
    print(age)
    print(business)

if __name__ == '__main__':
    main()

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests

class People(object):
    def __init__(self, name = "", place_of_birth = "", year_of_graduation = ""):
        self.name = name
        self.place_of_birth = place_of_birth
        self.year_of_graduation = year_of_graduation
        
class Ballotpedia(object):
    def __init__(self, driver, urls):
        self.driver = driver
        self.urls = urls

    def Parser(self):
        self.go_to_search()
        self.get_links()
        self.people_scraping()

    def go_to_search(self):
        self.driver.get("https://ballotpedia.org/Main_Page")

        search = self.driver.find_element_by_id("searchInput")
        search.send_keys("Bachelor's Stanford University")

        self.driver.find_element_by_class_name("bp-header-search-go").click()

    def get_links(self):
        links = self.driver.find_elements_by_xpath("//ul[@class = 'mw-search-results']//a")

        for i in links:
            link = i.get_attribute("href")

            url = {
                'href': link
            }

            self.urls.append(url)

    def people_scraping(self):
        people = People()

        name = []
        place = []
        year = []

        counter = 0

        for i in self.urls:
            if counter < 10:
                self.driver.get(i['href'])

                page = requests.get(i['href'])
                soup = BeautifulSoup(page.content, 'html.parser')

                try:
                    people_name = self.driver.find_element_by_xpath("//h1[@id = 'firstHeading']//span").text
                    people.name = people_name
                    name.append(people.name)

                except NoSuchElementException:
                    people.name = "NONE"
                    name.append(people.name)

                widget_row = soup.find_all(class_="widget-row")

                if widget_row[-1].find(class_='widget-key'):
                    if widget_row[-1].find(class_='widget-key').text == "Birthplace":
                        people_place_of_birth = widget_row[-1].find(class_="widget-value").text
                        people.place_of_birth = people_place_of_birth
                        place.append(people.place_of_birth)

                    else:
                        people.place_of_birth = "NONE"
                        place.append(people.place_of_birth)

                elif widget_row[-1].find('a'):
                    if widget_row[-3].find(class_='widget-key').text == "Birthplace":
                        people_place_of_birth = widget_row[-3].find(class_="widget-value").text
                        people.place_of_birth = people_place_of_birth
                        place.append(people.place_of_birth)

                    else:
                        people.place_of_birth = "NONE"
                        place.append(people.place_of_birth)

                else:
                    people.place_of_birth = "NONE"
                    place.append(people.place_of_birth)

                for widget in widget_row:
                    if widget.find(class_="widget-key") in widget:
                        widget_key = widget.find(class_="widget-key").text

                        if widget_key == "Bachelor's":
                            year_of_graduation = widget.find(class_="widget-value").text
                            people.year_of_graduation = year_of_graduation.split()[-1]
                            year.append(people.year_of_graduation)

                            if people.year_of_graduation.isalpha():
                                people.year_of_graduation = "NONE"
                                year.append(people.year_of_graduation)
                            break
            else:
                break

                print(people)

            counter = counter + 1

        data = pd.DataFrame({
            'NAME': name,
            'BIRTHPLACE': place,
            'YEAR OF GRADUATION': year,
        })

        data.to_csv('file.csv')

def main():
    driver = webdriver.Chrome()
    urls = []
    parser = Ballotpedia(driver, urls)
    parser.Parser()

if __name__ == '__main__':
    main()

#We import libraries and creating the driver
#import the driver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

import pandas as pd

#We give the website in which we want
website = 'https://www.adamchoi.co.uk/overs/detailed'

#The path 
path = '/home/exporter/Downloads/chromedriver'

#the driver
driver = webdriver.Chrome(service=ChromeService(executable_path=path))

#to open the website link
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, "./td[1]").text)
    home_team.append(match.find_element(By.XPATH, "./td[2]").text)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)

#to close browser
driver.quit()

df = pd.DataFrame({'date' : date, 'home_team' : home_team, 'score' : score, 'away_team' : away_team})

df.to_csv('football_data.csv', index=False)

print(df)
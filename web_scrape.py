from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('./chrome-win64/chrome.exe')

browser.get(start_url)
time.sleep(10)

def scrape():
    heading = ['NAME','LIGHT-YEARS FROM EARTH','PLANET MASS','STELLAR MAGNITUDE','DISCOVERY DATE']
    
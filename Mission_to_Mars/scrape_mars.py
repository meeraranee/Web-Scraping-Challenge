import pandas as pd 
from splinter import Browser
from bs4 import BeautifulSoup
import requests


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless = False)

def scrape():
    browser = init_browser()

def news_scrape():
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

# make yoself a dictionary girl, extra ice
    mars_data = {
        ""
    }



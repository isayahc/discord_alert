from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

from time import sleep

# finds all elements by the name
# find_elements_by_class_name is based on regex and not equal,
# there it's import to take out any elements that are not an exact match
# also, the article released todday will have "Today" in the text

def set_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    # I had to add an user agent
    chrome_options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    return driver


def get_today_link()-> str:
    # this needs to get edited
    """Goes on seekingalpha.com 

    Returns:
        str: The link of Today's Wallstreet breakfast article If it has been published
        else it returns an empty string
    """
    
    driver = set_driver()
    link = 'https://seekingalpha.com/author/wall-street-breakfast#regular_articles'
    driver.get(link)
    
    driver.implicitly_wait(60*2) # allows loading

    class_name = 'author-single-article'
    # div tage for articles  

    articles = driver.find_elements_by_class_name(class_name)
    for article in articles:

        article_text = article.text
        # other than Today and Yesterday, all other dates 
        # are formatted differently
        if 'Today' in article_text:
            x = article.find_elements_by_tag_name('a')

            article_link_element = x[0]
            article_link_element.click()
            # sends driver to article
            current_link = driver.current_url
            driver.close()

            return current_link
    
    #if this point is reach then the articles hasn't yet been published
    driver.close()
    # if today's article isn't yet publish return empty string
    return ""

def wait_for_update():
    #waits several times until today's article is up. 
    #start checking at time t UTC, and check every x minutes
    pass


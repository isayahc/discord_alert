from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import os

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
    chrome_options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; a_tag64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    return driver


def get_today_link()-> str:
    # this needs to get edited
    """Goes on seekingalpha.com. This to my knowledge is the best i could do with refactoring based
    on the structure of the website

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
            a_tag = article.find_elements_by_tag_name('a')

            try:

                article_link_element = a_tag[0]
                article_link_element.click()
                # sends driver to article
                current_link = driver.current_url
            except ElementClickInterceptedException:
                article_link_element = a_tag[1]
                article_link_element.click()
                # sends driver to article
                current_link = driver.current_url
            finally:
                driver.close()

            return current_link
    
    #if this point is reach then the articles hasn't yet been published
    driver.close()
    # if today's article isn't yet publish return empty string
    return ""

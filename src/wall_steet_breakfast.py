from selenium import webdriver

from time import sleep


# finds all elements by the name
# find_elements_by_class_name is based on regex and not equal,
# there it's import to take out any elements that are not an exact match
# also, the article released todday will have "Today" in the text

def get_today_link()-> str:
    """Goes on seekingalpha.com 

    Returns:
        str: The link of Today's Wallstreet breakfast article
    """
    
    driver = webdriver.Firefox()
    link = 'https://seekingalpha.com/author/wall-street-breakfast#regular_articles'
    driver.get(link)

    sleep(20) # allows loading

    class_name = 'author-single-article'
    # div tage for articles  

    articles = driver.find_elements_by_class_name(class_name)
    for article in articles:

        article_text = article.text
        # other than Today and Yesterday, all other dates 
        # are formatted differently
        if 'Today' in article_text:
            # print(article_text)
            x = article.find_elements_by_tag_name('a')

            article_link_element = x[0]
            article_link_element.click()
            # sends driver to article
            current_link = driver.current_url
            driver.close()

            return current_link

def wait_for_update():
    #waits several times until today's article is up. 
    #start checking at time t UTC, and check every x minutes
    pass


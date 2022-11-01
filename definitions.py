from selenium.webdriver.common.by import By

TAG_NAME = By.TAG_NAME
CLASS_NAME = By.CLASS_NAME
XPATH = By.XPATH
ID = By.ID
CSS_SELECTOR = By.CSS_SELECTOR

class Section:
    def __init__(self, link):
        self.link = link
        self.topics = []

class Topic:
    def __init__(self, link, title, content):
        self.link = link
        self.title = title
        self.content = content

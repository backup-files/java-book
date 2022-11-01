from selenium.webdriver.common.by import By
from dataclasses import dataclass

TAG_NAME = By.TAG_NAME
CLASS_NAME = By.CLASS_NAME
XPATH = By.XPATH
ID = By.ID
CSS_SELECTOR = By.CSS_SELECTOR

class Section:
    def __init__(self, link):
        self.link = link
        self.topics = []
    
    def add_topic(self, topic):
        self.topics.append(topic)

@dataclass
class Topic:
    link: str
    title: str
    content: str

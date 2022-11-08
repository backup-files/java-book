from selenium.webdriver.common.by import By
from dataclasses import dataclass
from typing import List

TAG_NAME = By.TAG_NAME
CLASS_NAME = By.CLASS_NAME
XPATH = By.XPATH
ID = By.ID
CSS_SELECTOR = By.CSS_SELECTOR

@dataclass
class Topic:
    link: str
    title: str
    content: str

@dataclass
class Section:
    link: str
    title: str
    topics: List[Topic]
    
    def add_topic(self, topic: Topic):
        self.topics.append(topic)

MAIN_LINK = ""
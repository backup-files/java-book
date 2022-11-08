from time import sleep 
from driver import driver


def get_link(url: str, duration: int=5):
    """
    Use selenium driver get method to send a get request and retrieve a response and wait for 'duration' seconds
    
        Parameters:
            url (str): The url for which the get request is for
            duration (int, optional): The duration for which the function should wait

        Returns:
            nothing
    """
    driver.get(url)
    sleep(duration)
import logging
import os

LOG_FILE = r'latest_log.txt'

if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

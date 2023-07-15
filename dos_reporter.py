import requests
import os
import subprocess
import time
import datetime
import threading
from colorama import Fore, Back, Style
import colorama
import logging

# Setup logging
logging.basicConfig(filename='screenshot_log.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Initialize the colorama module
colorama.init(autoreset=True)


def dos_website(url):

    # Test the website for dos attack vulnerability
    # subprocess.run(['./dos-tool.sh'], shell=True)
    subprocess.run(['ping', url])


def capture_screenshot(url, screenshot_duration):
    """
    Take a screenshot every 5 seconds for the specified duration.
    :param url:
    :param screenshot_duration:
    :return:
    """

    start_time = time.time()

    while True:

        # exit the loop if screenshot_duration seconds have passed
        if time.time() - start_time > screenshot_duration:
            break

        # Get the current date and time
        now = datetime.datetime.now()

        # Format it as a string
        now_str = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Set the screenshot filename
        screenshot_filename = f"screenshot_{now_str}.png"

        response = requests.get(url)

        # Print the HTTP headers
        # print(f"Headers: {response.headers}")

        print(f"Status: {response.status_code} {response.reason}")

        # Print the HTML content of the page
        # print(f"Content: {response.text}")

        # Log the screenshot
        logging.info(f"Took screenshot: {screenshot_filename}")

        # Wait for 5 seconds between screenshots
        time.sleep(5)


# Create threads for each function
t1 = threading.Thread(target=dos_website, args=("example.com",))
t2 = threading.Thread(target=capture_screenshot, args=("http://example.com", 900))


# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

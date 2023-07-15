from selenium import webdriver
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
    subprocess.run(['ping'], url)


def capture_screenshot(url, screenshot_duration):
    """
    Take a screenshot every 5 seconds for the specified duration.
    :param url:
    :param screenshot_duration:
    :return:
    """

    # specify the path to chromedriver if it's not in your PATH
    driver = webdriver.Chrome('ChromeDriver/chromedriver')

    driver.get(url)

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

        # Take a screenshot using Selenium
        driver.save_screenshot(screenshot_filename)

        # Log the screenshot
        logging.info(f"Took screenshot: {screenshot_filename}")

        # Wait for 5 seconds between screenshots
        time.sleep(5)

    # Close the browser after the loop is finished
    driver.quit()

# Create threads for each function
t1 = threading.Thread(target=dos_website("http://example.com"))
t2 = threading.Thread(target=capture_screenshot("http://example.com", 900))

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

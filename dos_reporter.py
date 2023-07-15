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


def dos_website():

    # Test the website for dos attack vulnerability
    subprocess.run(['./dos-tool.sh'], shell=True)


def capture_screenshot(url):
    while True:
        # Get the current date and time
        now = datetime.datetime.now()

        # Format it as a string
        now_str = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Set the screenshot filename
        screenshot_filename = f"screenshot_{now_str}.png"

        # The command to be executed
        screenshot_cmd = [
            "google-chrome-stable", "--headless", "--disable-gpu", "--screenshot",
            "--window-size=1280x1024", "--virtual-time-budget=2000", "--no-sandbox",
            f"--url={url}"
        ]

        # Execute the command
        subprocess.run(screenshot_cmd)

        # Rename the screenshot
        os.rename("screenshot.png", screenshot_filename)

        # Log the screenshot
        logging.info(f"Took screenshot: {screenshot_filename}")

        # Wait for 5 seconds
        time.sleep(5)


# Create threads for each function
t1 = threading.Thread(target=dos_website)
t2 = threading.Thread(target=capture_screenshot("http://example.com"))

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

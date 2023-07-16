import requests
import os
import subprocess
import time
import datetime
import threading
from colorama import Fore, Back, Style
import colorama
import logging
from log_setup import dos_logger, target_status_logger, log_response

# Initialize the colorama module
colorama.init(autoreset=True)


def dos_website(url):

    dos_logger.info(f"Beginning DoS attack on {url}")

    print(Fore.RED + f"Beginning DoS attack on {url}")

    # Test the website for dos attack vulnerability
    # subprocess.run(['./dos-tool.sh'], shell=True)

    # For testing purposes, use the ping command instead of slowhttptest
    subprocess.run(['ping', url])



def check_target_status(url, attack_duration):
    """
    Take a screenshot every 5 seconds for the specified duration.
    :param url:
    :param attack_duration:
    :return:
    """

    target_status_logger.info(f"Checking status of {url} every 5 seconds for {attack_duration} seconds")

    start_time = time.time()

    while True:

        # exit the loop if attack_duration seconds have passed
        if time.time() - start_time > attack_duration:
            break

        response = requests.get(url)

        if response.status_code == 418:

            target_status_logger.info(f"Response: {response.status_code} {response.reason}")

        else:

            target_status_logger.info(f"Response: {response.status_code} {response.reason}")

            log_response(response)


            # for key, value in response.headers.items():
            #
            #     target_status_logger.info(f"{key}: {value}")
            #
            # target_status_logger.info(f"{response.text}")

        # Wait for 5 seconds between screenshots
        time.sleep(5)


# Create threads for each function
t1 = threading.Thread(target=dos_website, args=("example.com",))
t2 = threading.Thread(target=check_target_status, args=("http://example.com", 900))


# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

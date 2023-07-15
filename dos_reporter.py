import subprocess
import time
import threading


def modify_website():
    # call your shell script (modify-website.sh)
    subprocess.run(['./dos-tool.sh'], shell=True)


def capture_screenshot(url):
    # You may need to adjust this path based on where you installed EyeWitness
    eyewitness_script_path = "/path/to/EyeWitness/EyeWitness.py"

    # The command to be executed
    cmd = f"python3 {eyewitness_script_path} --web --single {url}"

    while True:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()
        time.sleep(5)


# Create threads for each function
t1 = threading.Thread(target=modify_website)
t2 = threading.Thread(target=capture_screenshot("http://example.com"))

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

from selenium import webdriver
import sys
import os
import subprocess
import shutil
import time
from config import config

filename = f"cgra-t{config['turma']}g{config['grupo']}-"
shouldZip = config['zip']
shouldScreenshot = config['screenshot']


def printUsage():
    print("Usage:\npython3 main.py directory tpN\n")

def zipCWD(tag, outDirectory):
    shutil.make_archive(outDirectory + "/" + filename + tag, 'zip', os.getcwd())

def takeScreenshot(tag, outDirectory, driver):
    if(driver):
        driver.get("http://127.0.0.1:8080/" + tag.split('-')[0] + "/")
        time.sleep(1)
        wd = os.getcwd()
        os.chdir(outDirectory)
        driver.get_screenshot_as_file(filename + tag + ".png")
        os.chdir(wd)

def processTag(tag, outDirectory, driver=None):
    subprocess.run(["git", "checkout", tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if(shouldZip):
        zipCWD(tag, outDirectory)
    if(shouldScreenshot):
        takeScreenshot(tag, outDirectory, driver)

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        printUsage()
        return 1

    directory = sys.argv[1]
    tp = sys.argv[2]

    wd = os.getcwd()
    os.chdir(directory)
    tags = subprocess.check_output(["git", "tag", "-l"]).decode("utf-8").split('\n')
    tags = [i for i in tags if i.startswith(tp)]

    driver = None
    if(shouldScreenshot):
        driver = webdriver.Firefox()
        subprocess.Popen(["python3", "-m", "http.server", "8080"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for tag in tags:
        processTag(tag, wd, driver)

    if(driver):
        driver.close()

if __name__ == "__main__":
    main()

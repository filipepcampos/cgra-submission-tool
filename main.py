import sys
import os
import subprocess
import shutil
import webbrowser
import mss

def printUsage():
    print("Usage:")

def zipCWD(tag, outDirectory):
    print("Zipping")
    curDir = os.getcwd()
    os.chdir(outDirectory)
    shutil.make_archive(tag, 'zip', os.getcwd())
    os.chdir(curDir)

def processTag(tag, outDirectory):
    print(tag)
    subprocess.run(["git", "checkout", tag])
    zipCWD(tag, outDirectory)


def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        printUsage()

    directory = sys.argv[1]
    tag_template = sys.argv[2]

    wd = os.getcwd()

    os.chdir(directory)
    tags = subprocess.check_output(["git", "tag", "-l"]).decode("utf-8").split('\n')
    tags = [i for i in tags if i.startswith(tag_template)]

    #subprocess.run(["python3", "-m", "http.server", "8080"])
    for tag in tags:
        processTag(tag, wd)



if __name__ == "__main__":
    main()

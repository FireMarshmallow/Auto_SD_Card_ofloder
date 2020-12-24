import csv
import os
import shutil
import sys
import time
from time import sleep

# list of paths to sd cards / drives
def path_to_drive():
    list = [
        "/Volumes/NO NAME/",  # SD card from osmo action
        "/Volumes/Untitled 1/DCIM/100MEDIA/",  # SD card two
        "/Volumes/EOS_DIGITAL/DCIM/100CANON/",
    ]  # SD card From canon
    return list


# cherk if drives are connected
def if_connected():
    for path in path_to_drive():
        if os.path.exists(path) == True:
            offlode_card(path)


# move files off sd card
def offlode_card(sd):
    # walk directory
    move_to = "//Volumes/WinInstall/hellow"
    for dirName, subdirList, fileList in os.walk(sd, topdown=False):
        for fname in fileList:
            pathtofile = dirName + "/" + fname
            try:
                shutil.move(pathtofile, move_to)
            except:
                pass


# infenat loop
while True:
    if_connected()
    sleep(6)
    print("working")


# formeat sd?

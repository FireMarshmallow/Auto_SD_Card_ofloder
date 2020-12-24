import csv
import os
import shutil
import sys
import time
from time import sleep

# add paths to SD cards


def path_to_drive():
    list = ['/Volumes/NO NAME/DCIM/',  # SD card from osmo action
            '/Volumes/Untitled 1/DCIM/100MEDIA/',  # SD card two
            '/Volumes/EOS_DIGITAL/DCIM/100CANON/', ]  # SD card From canon
    return list

# cherk if drives are connected


def if_connected():
    for path in path_to_drive():
        if os.path.exists(path) == True:
            offlode_card(path)


# oflode to drives
def offlode_card(sd):
    move_to = '//Volumes/WinInstall/hellow'
    shutil.move(sd, move_to)


for _ in range(100):
    if_connected()
    sleep(6)
    print('working')

# infenat loop


# formeat sd?

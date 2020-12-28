import os
from shutil import move
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
    # gets path from list
    for path in path_to_drive():
        # checks if the drive is conected
        if os.path.exists(path) == True:
            # tells the offlode def drive is conected
            offlode_card(path)
            # passes the path


# move files off sd card
def offlode_card(sd):
    # path to the directore to move files to
    move_to = "//Volumes/WinInstall/hellow"
    # walks the directory
    for dirName, subdirList, fileList in os.walk(sd, topdown=False):
        for fname in fileList:
            # comdins to path with the file name
            pathtofile = dirName + "/" + fname
            # trys to move the fils or skips it
            try:
                print("moving: " + fname)
                move(pathtofile, move_to)
            except:
                pass


# infenat loop
while True:
    print("scaning")
    if_connected()
    sleep(6)

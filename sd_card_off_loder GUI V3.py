import datetime
import os
import threading
import tkinter as tk
from shutil import copy2
from time import sleep
from tkinter import *
from tkinter import filedialog
import sys
import csv

root = Tk()
root.title("Drive offloder")


def switchon():
    global switch
    switch = True
    print("scaning Started")
    start_drive_offlode()


def switchoff():
    print("scaning Stoped")
    global switch
    switch = False


def kill():
    root.destroy()


global listofsdcards
listofsdcards = []

###SAVE###


def make_save_file():
    PathAndName = os.path.join(sys.path[0], "SD_Cards_save")
    if os.path.exists(PathAndName) == False:
        with open(PathAndName, "a") as SD_save_csvfile:
            writer = csv.DictWriter(SD_save_csvfile, fieldnames="")
            writer.writeheader()
    return PathAndName


def Save():
    with open(make_save_file(), "w") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(listofsdcards)


def open_save():
    try:
        # gets the curent systom path and conbins it with the save file name
        PathAndName = os.path.join(sys.path[0], "SD_Cards_save")
        # makes and opans the save file
        with open(PathAndName, "r") as plants_csv:
            plants_readed = csv.reader(plants_csv, delimiter=",")
            for plants_row in plants_readed:  # fix this it just looks bad
                for savedpath in plants_row:
                    listofsdcards.append(savedpath)
    except:
        pass


###########


def Add_Sd_Card():
    listofsdcards.append(filedialog.askdirectory())
    updatelist()
    print(listofsdcards)


def start_drive_offlode():
    def Run():
        while switch == True:

            # cherk if drives are connected

            def if_connected():
                # gets path from list
                for path in listofsdcards:
                    # checks if the drive is conected
                    if os.path.exists(path) == True:
                        # tells the offlode def drive is conected
                        offlode_card(path)
                        # passes the path

            # move files off sd card

            def offlode_card(sd):
                # path to the directore to move files to
                move_to = "/Volumes/WinInstall/one"
                # walks the directory
                for dirName, subdirList, fileList in os.walk(sd, topdown=False):
                    for fname in fileList:
                        # comdins to path with the file name
                        pathtofile = dirName + "/" + fname
                        pathtopop = move_to + "/" + fname
                        if os.path.exists(pathtopop) == False:
                            print("moving: " + fname)
                            copy2(pathtofile, move_to)
                        else:
                            print(fname + " duplcet")

            print("scaning")
            if_connected()
            sleep(6)

    thread = threading.Thread(target=Run)
    thread.start()

    ###List box###


listbox_widget = tk.Listbox(root)


def updatelist():
    listbox_widget.delete(0, tk.END)
    for entry in listofsdcards:
        listbox_widget.insert(tk.END, entry)


def setup():
    pass


SaveButton = tk.Button(
    root,
    text="Save",
    activeforeground="blue",
    height=3,
    width=15,
    command=lambda: [Save()],
)

apendbutton = tk.Button(root, height=3, width=15, text="Add Path", command=Add_Sd_Card)

Start_scan = tk.Button(root, height=3, width=15, text="Start Scaning", command=switchon)
stop_scan = tk.Button(root, height=3, width=15, text="Stop scaning", command=switchoff)
killbutton = tk.Button(
    root, height=3, width=15, text="EXIT", command=lambda: [kill(), switchoff()]
)

###plasments###
listbox_widget.grid(row=0, column=0)
Start_scan.grid(row=1, column=0)
stop_scan.grid(row=2, column=0)
apendbutton.grid(row=3, column=0)
SaveButton.grid(row=4, column=0)
killbutton.grid(row=5, column=0)
######

open_save()
updatelist()
root.mainloop()

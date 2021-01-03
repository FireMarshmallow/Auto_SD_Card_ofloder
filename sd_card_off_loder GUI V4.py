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
import pickle

root = Tk()
root.title("Drive offloder")


def switchon():
    global switch
    switch = True
    print("scaning Started")
    changeTextStart()
    start_drive_offlode()


def switchoff():
    print("scaning Stoped")
    global switch
    changeTextstop()
    switch = False


def kill():
    root.destroy()


global listofsdcards
listofsdcards = []
global copy_to_path
copy_to_path = ""

###SAVE###
def save_file_path():
    PathAndName = os.path.join(sys.path[0], "SD_Cards_save.dat")
    return PathAndName


def Save(listofsdcards, copy_to_path):
    thing_to_save_for_next_time = [
        listofsdcards,
        copy_to_path,
    ]
    outfile = open(save_file_path(), "wb")
    pickle.dump(thing_to_save_for_next_time, outfile)
    outfile.close()


def open_save():
    try:
        infile = open(save_file_path(), "rb")
        new_dict = pickle.load(infile)
        infile.close()
        for item in new_dict[0]:
            listofsdcards.append(item)
        global copy_to_path
        copy_to_path = new_dict[1]
        updatelist()
        changeTextOutPath()
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
                # walks the directory
                for dirName, subdirList, fileList in os.walk(sd, topdown=False):
                    for fname in fileList:
                        # comdins to path with the file name
                        pathtofile = dirName + "/" + fname
                        pathtopop = copy_to_path + "/" + fname
                        if os.path.exists(pathtopop) == False:
                            print("Copying: " + fname)
                            copy2(pathtofile, copy_to_path)
                        else:
                            print(fname + " duplcet")

            print("scaning")
            if_connected()
            sleep(6)

    thread = threading.Thread(target=Run)
    thread.start()


def move_to_folder():
    global copy_to_path
    copy_to_path = filedialog.askdirectory()
    changeTextOutPath()


###List box###


listbox_widget = tk.Listbox(root)


def updatelist():
    listbox_widget.delete(0, tk.END)
    for entry in listofsdcards:
        listbox_widget.insert(tk.END, entry)


SaveButton = tk.Button(
    root,
    text="Save",
    activeforeground="blue",
    height=3,
    width=15,
    command=lambda: [Save(listofsdcards, copy_to_path), changeTextSaved()],
)

apendbutton = tk.Button(root, height=3, width=15, text="Add drive", command=Add_Sd_Card)
Start_scan = tk.Button(root, height=3, width=15, text="Start Scaning", command=switchon)
killbutton = tk.Button(
    root, height=3, width=15, text="EXIT", command=lambda: [kill(), switchoff()]
)

outpath = tk.Button(
    root,
    text="Select output folder",
    activeforeground="blue",
    height=3,
    width=15,
    command=move_to_folder,
)


def changeTextSaved():
    SaveButton["text"] = "Saved"


def changeTextOutPath():
    outpath["text"] = copy_to_path


def changeTextStart():
    Start_scan["text"] = "Stop"
    Start_scan["command"] = switchoff


def changeTextstop():
    Start_scan["text"] = "Start"
    Start_scan["command"] = switchon


###plasments###
outpath.grid(row=1, column=0)
Start_scan.grid(row=2, column=0)
listbox_widget.grid(row=0, column=0)
apendbutton.grid(row=4, column=0)
SaveButton.grid(row=5, column=0)
killbutton.grid(row=6, column=0)
######

open_save()
updatelist()
root.mainloop()

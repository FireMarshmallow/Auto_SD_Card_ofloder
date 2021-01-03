import pickle
import os, sys

global copy_to_path
listofsdcards = []
copy_to_path = ""

# outfile = open(filename, "wb")
# pickle.dump(all_lists, outfile)
# outfile.close()


# infile = open(filename, "rb")
# new_dict = pickle.load(infile)
# infile.close()

# #######
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
    except:
        pass


# Save(listofsdcards, copy_to_path)
open_save()

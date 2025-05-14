import os
import glob
import numpy as np

questionsWithoutGuide = np.genfromtxt(fname="../../Desktop/noguide.txt")
questionsWithGuide = np.genfromtxt(fname="../../Desktop/withguide.txt")


def read_txt_files(directory_path):
    """
    Reads all .txt files from folder withGuide withoutGuide.
    Returns .tet file
    """
    # Use glob to get all .txt files in the directory
    txt_files = glob.glob(os.path.join(directory_path, '*.txt'))

    # List to store the contents of each file
    contents_list = []

    # Loop through the list of .txt files and read their contents
    for txt_file in txt_files:
        with open(txt_file, 'r', encoding='utf-8') as file:
            content = file.read()
            contents_list.append(content)
    return contents_list

eventsWithoutGuide = read_txt_files('C:/Users/David/Documents/Bachelor/Results_Playtest/Results_ohneGuide')
eventsWithGuide = read_txt_files('C:/Users/David/Documents/Bachelor/Results_Playtest/Results_mitGuide')

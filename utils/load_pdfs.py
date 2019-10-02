import os

def getFileNames():
    foldername = 'papers'
    file_names = os.listdir(foldername)
    return foldername, file_names
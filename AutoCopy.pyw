from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import json
import os.path
from os import path
from pathlib import Path



home = str(Path.home())
class MyHandler(FileSystemEventHandler):
 
    i=1
    def on_any_event(self, event):

        for filename in os.listdir(folder_to_track):
            filetype = os.path.splitext(filename)
            print (filetype)
            filetypeExtTup = list(filetype).pop(1)
            if filetypeExtTup == "":
                filetypeExt = "_Folders"
            else:
                filetypeExt = filetypeExtTup[1:]
            path = convertTuple(home + '/Files/' + filetypeExt)
            
            if os.path.exists(path):
                folder_destination = path
            elif not os.path.exists(path):
                os.mkdir(path)
                folder_destination = path
            else:
                print ("ERROR")
                return
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = home + "/Organizer"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()



        

def grabFiles():
    
    copy_tree(home +"/Documents/Test Folder", home +"/Documents/Transfer Folder")
    print("Copied Files")
    from distutils.dir_util import copy_tree

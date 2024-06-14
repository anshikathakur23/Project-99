import time
import os
import shutil

def __deleteFiles__ ():
    currentTime =  time.time ()

for root, dirs, files in os.walk ():
    path = os.path.join (root, files)

path = "Enter your folder path"

__deleteFiles__ (path)

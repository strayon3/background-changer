import argparse
import os
import time
import random
import requests
import ctypes
import platform
from PIL import Image
import glob

img_list = []
temp = []
path = "C:/Users/stray/Desktop/webscraping notebooks/backgrounds/"
# read imgs from folder store them in a list 
def get_img(img_list):
   
    for filename in os.listdir(path):
        if(filename.endswith('.png') or filename.endswith('.jpg') ):
            img_list.append(filename)
            
    
    #chosse a random img from list 
    pick = random.choice(img_list)
    temp.append(pick)
    print(pick)


#display img as background 

    

    #check operating system
    system_name = platform.system().lower()
    path1 = ""
    if system_name == 'linux':
        path1 = os.getcwd()+ pick
        command = "gsettings set org.gnome.desktop.background picture.uri file:" + path+pick
        os.system(command)
    elif system_name == "windows":
        path1 =  path + pick
        ctypes.windll.user32.SystemParametersInfoW(20,0,path1,0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Enter time in minutes")

    args = parser.parse_args()
    minute = int(args.time)
    while(True):
        time.sleep(minute*60)
        get_img(img_list)

#todo for future 
#random choice system isnt really random needs to pull from whole list 
#could be cleaned up and optomized a little more
#img file could be bigger 
#implement an auto converter for png and jpg types when reading in the file 
#
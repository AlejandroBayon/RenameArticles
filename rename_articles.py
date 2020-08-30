#!/usr/bin/env python3

#import modules
import os
import sys
import shutil
import re

#store the directory where the files to be renamed are located
directory = sys.argv[1]

#make a list of the files to be renamed
article_list = os.listdir(directory)

#create a new directory to save the renamed files
new_directory = directory + r"\Renamed"
os.mkdir(new_directory)

#copy each file in the new directory changing the name
n = 0
for article in article_list:
    name = re.search(r"(.*) ([0-9]*) - (.*)",article)
    new_article = name[2] + " " + name[1] + " - " + name[3]
    shutil.copyfile(directory + "\\" + article, new_directory + "\\" + new_article)
    n += 1

print("{} files renamed succesfully!".format(n))
x = input("Press any key to exit...")
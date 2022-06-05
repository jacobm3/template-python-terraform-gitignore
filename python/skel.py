#!/usr/bin/python3

import argparse
import datetime
import json
import os
import pprint
import re
import requests
import sqlite3
import sys
import time

#import numpy as np
#import pandas as pd

p=print
pp=pprint.pprint

#from bs4 import BeautifulSoup as bs



# ts = datetime.datetime.now().isoformat()

def options():
    'Parse command line options with argparse.'

    global options,args,debug
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="debug", action='store_true', help="print debug information")
    parser.add_argument("-l", dest="feedlistfile", help='filename with list of feeds, one URL per line')
    options = parser.parse_args()

    # if not options.feedlistfile:
    #     print("\nError: Must specify -l <feed list file>\n")
    #     parser.print_help()
    #     sys.exit(1)

def func():
    pass
  
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  count = 0
while (count < 3):    
    count = count + 1
    print("Hello Geek")
    
    np.arange(-3, 3, 0.5, dtype=int)
    
    

if __name__ == '__main__':
    pass
    func()

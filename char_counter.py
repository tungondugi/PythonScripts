#!/usr/local/bin/python3.8

import sys

"""
    This script counts the number of:
    1.) number of characters;
    2.) number of words;
    3.) number of lines;
    from a file.
"""

# reading a file
def counter(filename):
    line = 0
    words = 0
    chars = 0
    
    #reading a file;
    with open(filename) as file:
        data = file.readlines()

        for element in data:
            
            #counting the number of lines in a file
            line += 1
            
            #counting the number of words in a file
            words += len(element.split())

            #counting the number of characters in a file
            for ele in element:
                chars += 1
        
    print(f"Number of charactes = {chars}.\nNumber of words = {words}.\nNumber of lines = {line}.")


#The main functions
if __name__ == "__main__":
    filename = sys.argv[1]
    counter(filename)

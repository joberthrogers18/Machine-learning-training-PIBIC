'''
Author: Joberth Rogers Tavares Costa
'''

import os
import argparse
import re


def remove_whitespace(current_list):
    # Function responsible to remove all
    # the blank itens in list and return it

    while '' in current_list:
        current_list.remove('')

    return current_list


def find_directory(file, offset, searched_directory, inode):
    # Using the fls to list the directories
    # Find the current search directory
    # and return the inode from the next visit directory

    fls = os.popen('fls -o ' + offset + ' ' + file + ' ' + inode).read()
    fls = fls.replace('\t', ' ').replace(':', '')    
    split_fls = fls.split('\n')
    split_fls = remove_whitespace(split_fls)

    for directory in split_fls:
        if re.search(r'\b' + searched_directory + r'\b', directory):
            next_directorie = directory.split(' ')
            break

    return next_directorie[1]


def main():
    # main function responsible for all the business rules from script

    parser = argparse.ArgumentParser()

    # arguments parser to guide the input scripts
    parser.add_argument(
        "-f",
        help="name of file that will be collected",
        required=True
    )
    parser.add_argument(
        "-d",
        help="Destination of file",
        required=True
    )

    # Make a mmls in the filesystem 
    # and give an split in output tree directories
    args = parser.parse_args()
    mmls = os.popen('mmls ' + args.f).read()

    split_mmls = mmls.split('\n')

    # Loking for the userdata directory
    for word in split_mmls:
        if "userdata" in word:
            offset_mmls = word.split(" ")
            break

    offset_mmls = remove_whitespace(offset_mmls) 

    # Path to go to the WhatsApp voice notes directory
    list_directorie = ['media', '0', 'WhatsApp', 'Media', 'WhatsApp Voice Notes']

    inode = ''

    # Go through the tree directories from file system
    # and when find the directories from list above
    # recover the inode from directory and
    # make a pop in list and part to next directory till the 
    # WhatsApp Voice Notes directory destination
    while True:
        inode = find_directory(args.f, offset_mmls[-4], list_directorie[0], inode)
        list_directorie.pop(0)

        if len(list_directorie) == 0: break

    # Send the files to the destination required by user
    os.popen('tsk_recover -o ' + offset_mmls[-4] + ' -d ' + inode + ' ' + args.f + ' ' + args.d).read()

if __name__ == "__main__":
    main()

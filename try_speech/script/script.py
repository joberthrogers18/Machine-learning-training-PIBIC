import os
import argparse
import re


def remove_whitespace(current_list):
    while '' in current_list:
        current_list.remove('')

    return current_list


def find_directory(file, offset, searched_directory):

    inode = ''

    fls = os.popen('fls -o ' + offset + ' ' + file + ' ' + inode).read()
    fls = fls.replace('\t', ' ').replace(':', '')
    split_fls = fls.split('\n')
    split_fls = remove_whitespace(split_fls)

    for directorie in split_fls:
        if re.search(r'\b' + searched_directory + r'\b', directorie):
            next_directorie = directorie.split(' ')
            inode = next_directorie[1]

    return inode

    
def main():
    parser = argparse.ArgumentParser()

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

    args = parser.parse_args()
    mmls = os.popen('mmls ' + args.f).read()

    split_mmls = mmls.split('\n')

    for word in split_mmls:
        if "userdata" in word:
            offset_mmls = word.split(" ")
            break

    offset_mmls = remove_whitespace(offset_mmls)
    
    list_directorie = ['media', '0', 'WhatsApp', 'Media', 'WhatsApp Voice Notes']

    inode = ''
    
    inode = find_directory(args.f, offset_mmls[-4], list_directorie[0])
    print(inode)
    '''  
    cont = 0
    while(list_directorie != [] or cont < 20):
        
        for directorie in list_directorie:
            for current_dir in split_fls:

                if directorie in current_dir:
                    print(current_dir)
        cont += 1'''

if __name__ == "__main__":
    main()

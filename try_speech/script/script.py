import os
import argparse


def remove_whitespace(current_list):
    while '' in current_list:
        current_list.remove('')

    return current_list


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
            print(offset_mmls)
            break

    offset_mmls = remove_whitespace(offset_mmls)
    


if __name__ == "__main__":
    main()

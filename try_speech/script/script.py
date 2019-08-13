import os
import argparse


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
    print(args.d, args.f)
    

# version = os.system("mmls -V")

# print(version)

if __name__ == "__main__":
    main()

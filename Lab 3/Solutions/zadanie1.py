import os
import sys

def main(args):
    files = os.listdir(args[1])

    for file in files:
        if file.endswith(args[2]):
            print(file)

if __name__ == "__main__":
    main(sys.argv)
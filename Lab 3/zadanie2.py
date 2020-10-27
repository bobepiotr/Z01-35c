import os
import sys

def tree_print(root, lvl, last):
    if lvl != 0:
        print("   ", end='')
        for i in range(lvl-1):
            print("|   ", end='')
        if last:
            print("└---", end='')
        else:
            print("|---", end='')
    print(os.path.split(root)[-1])

    if os.path.isdir(root):
        list = os.listdir(root)
        for i in range(len(list)):
            tree_print(os.path.join(root, list[i]), lvl+1, i == len(list)-1)


def main(args):
    tree_print(args[1], 0, False)


if __name__ == "__main__":
    main(sys.argv)

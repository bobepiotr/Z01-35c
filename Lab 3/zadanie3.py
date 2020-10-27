import sys

def main(args):
    numbers = []
    if (len(args) > 1):
        numbers = args[1].split(' ')
        try:
            numbers = list(map(lambda x: int(x), numbers))
        except ValueError:
            print("Integer list expected")
            return []

        numbers.sort()
    return numbers

if __name__ == "__main__":
    print(main(sys.argv))

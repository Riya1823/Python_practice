import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file1", help="file whose content to see")
parser.add_argument("file2", help="file whose content to see")

parser.add_argument("-n",default=5, type=int, help ="no.of lines from files")

args = parser.parse_args()

print(args)


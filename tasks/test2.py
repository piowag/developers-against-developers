import os.path
from os import path

def main():

    assert os.path.exists(os.path.expanduser('~/task_two.txt'))
    f = open(os.path.expanduser("~/task_two.txt"), "r")
    assert(f.read().strip() == "5")

if __name__== "__main__":
       main()
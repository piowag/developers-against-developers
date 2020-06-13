import os.path
from os import path

def main():

    assert os.path.exists('task_two.txt')
    f = open("task_two.txt", "r")
    assert(f.read() == "5")

if __name__== "__main__":
       main()
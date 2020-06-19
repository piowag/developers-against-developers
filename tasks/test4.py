# 2. Create a text file called "CreateMe".

import os.path
from os import path

def main():

    assert os.path.exists(os.path.expanduser('~/CreateMe.txt'))

if __name__== "__main__":
   main()
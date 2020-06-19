# 2. Create a directory called "CreateMe".

import os.path
from os import path

def main():

    assert os.path.exists(os.path.expanduser('~/task_one'))

if __name__== "__main__":
   main()
#3. Make directory called "Question3". In the directory "Question2", create the text document "TXT.txt" 
# containing the words "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

import os.path
from os import path

def main():

    assert os.path.exists('~/Question/TXT.txt')
    f = open("~/Question/TXT.txt", "r")
    assert(f.read() == "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

if __name__== "__main__":
       main()
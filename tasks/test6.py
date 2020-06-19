# Make a file "TXT_rights_of_use.txt" and change right of use on:
# - Read, save for owner. 
# - No rights for the rest.

import os
import stat

def main():

    f = os.path.expanduser("~/TXT_rights_of_use.txt")

    status = os.stat(f) 
    assert(oct(status.st_mode)[-3:] == "600")

if __name__== "__main__":
   main()


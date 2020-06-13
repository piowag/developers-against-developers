# Make a file "TXT_rights_of_use.txt" and change right of use on:
# - No rights for everyone.

import os
import stat

def main():

    f = "~/TXT_rights_of_use.txt"

    status = os.stat(f) 
    assert(oct(status.st_mode)[-3:] == "000")

if __name__== "__main__":
   main()


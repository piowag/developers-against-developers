# Make a file "TXT_rights_of_use.txt" and change the usage rights to:
# - Read, save, execution for owner,
# - Read, save for group,
# - No rights for other.

import os
import stat

def main():

    f = "~/TXT_rights_of_use.txt"

    status = os.stat(f) 
    assert(oct(status.st_mode)[-3:] == "760")

if __name__== "__main__":
   main()


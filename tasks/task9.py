#Create txt file named "UpAndDown" containing the words 

#"Lorem ipsum dolor sit amet consectetur adipiscing elit Ut vel congue magna Nunc semper ut ipsum at auctor Aenean varius eleifend condimentum.". 

#Change first letter to lower case, second letter to upper case, third letter to lower case etc. Spaces should be count as letters, but don't change them.
#Example:
#"Lorem ipsum dolor" -> "lOrEm iPsUm dOlOr".

import os

def main():

    assert os.path.isfile(os.path.expanduser('UpAndDown.txt'))
    f = open("UpAndDown.txt", "r")
    assert(f.read() == "lOrEm iPsUm dOlOr sIt aMeT CoNsEcTeTuR AdIpIsCiNg eLiT Ut vEl cOnGuE MaGnA NuNc sEmPeR Ut iPsUm aT AuCtOr aEnEaN VaRiUs eLeIfEnD CoNdImEnTuM.")

if __name__== "__main__":
       main()
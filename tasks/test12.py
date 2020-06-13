#Create txt file named "UpperLetters" containing the words 

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus volutpat cursus odio, sed molestie nulla tincidunt eu. Quisque in sem elit. 
# Maecenas scelerisque augue eu purus sodales dapibus. Phasellus sodales, massa vel convallis mollis, metus ante eleifend libero, eleifend porta erat tortor non augue. 
# Aliquam quis feugiat magna. Quisque non purus sed nisl pellentesque rutrum. Vivamus pellentesque et sem eu pretium. Suspendisse egestas tristique tincidunt. 
# Pellentesque purus felis, tincidunt a mollis id, imperdiet eu risus. Morbi vitae tellus est. Phasellus maximus lorem varius tortor egestas finibus vitae a justo. 
# Mauris sit amet pretium erat. Vivamus ac dui a ante venenatis posuere eu sed lacus. Maecenas vulputate metus sed gravida condimentum.". 

#Change ALL letters to upper letters.

import os

def main():

    assert os.path.isfile(os.path.expanduser('~/UpperLetters.txt'))
    f = open("~/UpperLetters.txt", "r")
    assert(f.read() == "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT. VIVAMUS VOLUTPAT CURSUS ODIO, SED MOLESTIE NULLA TINCIDUNT EU. QUISQUE IN SEM ELIT. MAECENAS SCELERISQUE AUGUE EU PURUS SODALES DAPIBUS. PHASELLUS SODALES, MASSA VEL CONVALLIS MOLLIS, METUS ANTE ELEIFEND LIBERO, ELEIFEND PORTA ERAT TORTOR NON AUGUE. ALIQUAM QUIS FEUGIAT MAGNA. QUISQUE NON PURUS SED NISL PELLENTESQUE RUTRUM. VIVAMUS PELLENTESQUE ET SEM EU PRETIUM. SUSPENDISSE EGESTAS TRISTIQUE TINCIDUNT. PELLENTESQUE PURUS FELIS, TINCIDUNT A MOLLIS ID, IMPERDIET EU RISUS. MORBI VITAE TELLUS EST. PHASELLUS MAXIMUS LOREM VARIUS TORTOR EGESTAS FINIBUS VITAE A JUSTO. MAURIS SIT AMET PRETIUM ERAT. VIVAMUS AC DUI A ANTE VENENATIS POSUERE EU SED LACUS. MAECENAS VULPUTATE METUS SED GRAVIDA CONDIMENTUM.")

if __name__== "__main__":
       main()
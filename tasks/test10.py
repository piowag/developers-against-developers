#Create txt file named "CapitalizedWords" containing the words 

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus volutpat cursus odio, sed molestie nulla tincidunt eu. Quisque in sem elit. 
# Maecenas scelerisque augue eu purus sodales dapibus. Phasellus sodales, massa vel convallis mollis, metus ante eleifend libero, eleifend porta erat tortor non augue. 
# Aliquam quis feugiat magna. Quisque non purus sed nisl pellentesque rutrum. Vivamus pellentesque et sem eu pretium. Suspendisse egestas tristique tincidunt. 
# Pellentesque purus felis, tincidunt a mollis id, imperdiet eu risus. Morbi vitae tellus est. Phasellus maximus lorem varius tortor egestas finibus vitae a justo. 
# Mauris sit amet pretium erat. Vivamus ac dui a ante venenatis posuere eu sed lacus. Maecenas vulputate metus sed gravida condimentum.". 

# Change first letter of ALL words to upper letter.

import os

def main():

    assert os.path.isfile(os.path.expanduser('~/UpperLetters.txt'))
    f = open("~/UpperLetters.txt", "r")
    assert(f.read() == "Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit. Vivamus Volutpat Cursus Odio, Sed Molestie Nulla Tincidunt Eu. Quisque In Sem Elit. Maecenas Scelerisque Augue Eu Purus Sodales Dapibus. Phasellus Sodales, Massa Vel Convallis Mollis, Metus Ante Eleifend Libero, Eleifend Porta Erat Tortor Non Augue. Aliquam Quis Feugiat Magna. Quisque Non Purus Sed Nisl Pellentesque Rutrum. Vivamus Pellentesque Et Sem Eu Pretium. Suspendisse Egestas Tristique Tincidunt. Pellentesque Purus Felis, Tincidunt A Mollis Id, Imperdiet Eu Risus. Morbi Vitae Tellus Est. Phasellus Maximus Lorem Varius Tortor Egestas Finibus Vitae A Justo. Mauris Sit Amet Pretium Erat. Vivamus Ac Dui A Ante Venenatis Posuere Eu Sed Lacus. Maecenas Vulputate Metus Sed Gravida Condimentum.")
    
if __name__== "__main__":
       main()
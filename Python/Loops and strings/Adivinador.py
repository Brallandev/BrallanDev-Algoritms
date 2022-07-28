# -*- coding: utf-8 -*-  

import random 

def run():
    number_found=False
    limit = int(input("Hasta que número"))
    generated_number= random.randint(1,limit)

    while not number_found:
        number= int(input("Cual es el número? \n"))
        if(number==generated_number):
            print("Eureka el número era: "+str(generated_number))
            number_found=True
        elif(number>generated_number):
            print("Menos")
        else:
            print("Más")

if __name__ == "__main__":
    run()
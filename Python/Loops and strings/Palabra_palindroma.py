# -*- Coding:utf8 -*- 
word=""
backword=""

def ask_word():
    global word
    word = input("Ingresa una pabalabra y te diremos si es magica \n")

def evaluate():
    global backword
    global word
    ask_word()
    backword = word[::-1]
    if(backword==word):
        print("La palabra es palíndroma")
    else:
        print("La palabra no es palíndroma")

if __name__ == "__main__":
    evaluate()
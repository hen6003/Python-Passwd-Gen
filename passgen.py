from random import randint

def gen():
    def evry():
        for i in range(int(pas)):
            a = randint(0, len(letters)- 1)
            print("\033[33m" + letters[a], end = "")
            
    def basic():
        for i in range(int(pas)):
            a = randint(26, 61)
            print("\033[33m" + letters[a], end = "")
            
    def special():
        for i in range(int(pas)):
            a = randint(26, len(letters)- 1)
            print("\033[33m" + letters[a], end = "")
            
    def bold():
        for i in range(int(pas)):
            a = randint(0, 61)
            print("\033[33m" + letters[a], end = "")
    
    letters = ["A", "B", "C", "D","E", "F", "G", "H","I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "9", "a", "b", "c", "d","e", "f", "g", "h","i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z", "/", "*", "(", ")", "@", "|", "£", "$", "%", "¬", "#", "[", "]", "-", "_", "+", "=", "<", ">", "^"]
    
    pas = input("\033[1m\033[36mHow Big Do You Want You're Password: \033[32m")
    
    typ = input("\033[36mType 's' for special ,'b' for bold,'a' for all or nothing for basic: \033[32m")
    
    if typ == "S" or typ == "s":
        special()
    
    elif typ == "B" or typ == "b":
        bold()
    
    elif typ == "A" or typ == "a":
        evry()
    
    else:
        basic()
        
    cont = input("\n\n\033[36mContinue y/N: \033[32m")
    
    if cont == "Y" or cont == "y":
        return
        
    else:
        exit()
        
while True:
    gen()

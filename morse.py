morseDict = {   'A':'.-', 'B':'-...', 
                'C':'-.-.', 'D':'-..', 'E':'.', 
                'F':'..-.', 'G':'--.', 'H':'....', 
                'I':'..', 'J':'.---', 'K':'-.-', 
                'L':'.-..', 'M':'--', 'N':'-.', 
                'O':'---', 'P':'.--.', 'Q':'--.-', 
                'R':'.-.', 'S':'...', 'T':'-', 
                'U':'..-', 'V':'...-', 'W':'.--', 
                'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-'
            }

def encrypt(message):
    cipher=''
    for letter in message:
        if letter!=' ':
            cipher+=morseDict[letter]+' '
        else:
            cipher+=' '
    return cipher

def decrypt(message):
    message+=' '
    decipher=''
    citext=''
    for letter in message:
        if letter!=' ':
            i=0
            citext+=letter
        else:
            i+=1
            if i==2:
                decipher+=' '
            else:
                decipher+=list(morseDict.keys())[list(morseDict.values()).index(citext)]
                citext=''
    return decipher

def main():
    try:
        choice=int(input('Press 1 to encrypt a message\nPress 2 to decrypt a message\nEnter your choice: '))
        print()

        if choice>2:
            print('Enter only 1 or 2')
            print()
            main()
        
        if choice==1:
            message=input('Enter a message to encrypt: ')
            print()
            result=encrypt(message.upper())
            print('Your encrypted message is:',result)
            print()
        
        elif choice==2:
            message=input('Enter a message to decrypt: ')
            print()
            result=decrypt(message.upper())
            print('Your decrypted message is:',result)
            print()

    except ValueError:
        print()
        print('Enter only 1 or 2')
        print()
        main()

if __name__ == "__main__":
    main()
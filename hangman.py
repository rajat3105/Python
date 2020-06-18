import random
from collections import Counter

fruits='''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
fruits=fruits.split()
word=random.choice(fruits)

if __name__ == "__main__":
    print('Guess the word!     HINT: Word is a name of a fruit')
    for i in word:
        print('_',end=' ')
    print()

    playing=True
    letterGuess=''
    chances=len(word)+2
    correct=0
    flag=0

    try:
        while chances!=0 and flag==0:
            print()
            chances-=1

            try:
                guess=str(input('Enter a letter: '))
            except:
                print('Enter only a letter')
            
            if not guess.isalpha():
                print('Enter a letter')
                continue
            elif len(guess)>1:
                print('Enter only single letter')
                continue
            elif guess is letterGuess:
                print('You have already guessed that letter')
                continue

            if guess in word:
                cnt=word.count(guess)
                for _ in range(cnt):
                    letterGuess+=guess
            
            for char in word:
                if char in letterGuess and (Counter(letterGuess)!=Counter(word)):
                    print(char,end=' ')
                    correct+=1
                elif (Counter(letterGuess)==Counter(word)):
                    print('The word is: '+word)
                    flag=1
                    print('You won!!')
                    break
                    break
                else:
                    print('_',end=' ')
            print()

        if chances<=0 and (Counter(letterGuess)!=Counter(word)):
            print()
            print('You lost!!')
            print('The word was: '+word)

    except KeyboardInterrupt:
        print()
        print('Bye!!')
        print()
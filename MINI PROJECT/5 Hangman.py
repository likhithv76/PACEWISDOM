import random

def Hangman():
 print ('TIME TO PLAY HANGMAN')

wordlist =['apples', 'oranges', 'grapes', 'pizza', 'cheese', 'burger']
secret = random.choice(wordlist)
guesses = 'aeiou'
turns = 5

while turns > 0:
     missed = 0
     for letter in secret:
         if letter in guesses:
             print (letter,end=' ')
         else:
           print ('_',end=' ')
           missed= missed + 1

     print

     if missed == 0:
         print ('\nYou win!')
         break

     guess = input('\nguess a letter: ')
     guesses += guess

     if guess not in secret:
         turns = turns -1
         print ('\nNope.')
         print ('\n',turns, 'more turns')
         if turns < 5: print ('\n  |  ')
         if turns < 4: print ('  O  ')
         if turns < 3: print (' /|\ ')
         if turns < 2: print ('  |  ')
         if turns < 1: print (' / \ ')
         if turns == 0:
             print ('\n\nThe answer is', secret)

playagain = 'yes'
while playagain == 'yes': 
    Hangman()
    print('Do you want to play again? (yes or no)')
    playagain = input()
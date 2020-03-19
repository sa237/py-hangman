import random
#from pip._vendor.html5lib._ihatexml import letter

def select_word():
    words = ['cornea','list','neck','dance','trim','insta','face','movie','orange','worm','crazy','motive','love','hate','modi','juice','mouse','python','dart']
    return random.choice(words)


word = select_word()
word_letters = list(word)

def check_letter(word,guesses,guess):
    status = ''
    matches = 0
    
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "*"
        
 
        if letter == guess:
            matches += 1
        
        
    
    if matches == 1:
        print ('you have guessed the letter correctly')
    else:
        print ('Entered input does not exist in the word ')
    return status

def main():
    print(word)
    no_of_guesses = 0
    guesses = []
    counter=0
    guessed = False
    test = '*' * len(word_letters)
    print ('Hello! the word is \"', test , '\" and it has ', len(word_letters),'letters, you should guess it now ')
    while not guessed:
        while no_of_guesses < len(word_letters) :
                guess = str(input('please input your letter '))
                if  len(guess) == 1:
                    no_of_guesses += 1
                    counter+=1
                if len(guess) == 1: 
                    guesses.append(guess)
                    result = check_letter(word, guesses, guess)
                    if '*' not in result :
                        guessed = True 
                    else:
                        print (result)
                else:
                    print ('you should enter only 1 letter at a time , please enter again' )
                if counter == len(word_letters):
                    print('No more guesses left!')
    print ('you found the the word: '+ word +' in '+ str(no_of_guesses) +' steps')            
    
    
main()

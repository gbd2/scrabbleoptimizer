from copy import deepcopy

scrabblepoints = {'A':1 , 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 
                  'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 
                  'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':8, 'W':4, 
                  'X':8, 'Y':4, 'Z':10}

def get_filewords(filename:str) -> list:
    with open(filename) as lines:
        return [line.split(None, 1)[0] for line in lines]

def legal_words_possible(letterdeck: list, filename: str) -> list:
    possiblewords = []
    wordlist = get_filewords(filename)

    for word in wordlist:
        cand = True
        tempdeck = deepcopy(letterdeck)
        for letter in word:
            if letter not in tempdeck:
                cand = False
                break
            else:
                tempdeck.remove(letter)
        if cand:
            possiblewords.append(word)

    return possiblewords

def bestword(possiblewords:list) -> dict:
    bestpts = 0
    best = ''
    wordletterlst = []
    wordpoints = {}
    idx = 0

    for wordidx in range(len(possiblewords)):
        templst = []
        for letter in possiblewords[wordidx]:
            templst.append(letter)
        wordletterlst.append(templst)
    
    for wordidx in range(len(possiblewords)):
        tempsum = 0
        for letter in possiblewords[wordidx]:
            tempsum += scrabblepoints[letter]
        wordpoints[possiblewords[wordidx]] = tempsum

    for word in possiblewords:
        if bestpts < wordpoints[word]:
            bestpts = wordpoints[word]
            best = word
    
    result = {best: bestpts}
    if result == {'':0}:
        return "Sorry, no words can be made with your deck."
    else:
        return result

def user_input() -> list:

    while True:
        userletters = str(input("Give up to seven letters in your deck (not case sensitive):"))

        if not all(char.isalpha() for char in userletters):
            print("Sorry, you can only use letters (no spaces, numbers, symbols, or emoticons).")
            continue
        else:
            break
    
    print("Thanks! Give me just a second...")
    
    userletters = userletters.replace(',','')
    userletters = userletters.replace(' ','')
    userletters = userletters.upper()

    return list(userletters)


def run_program():
    while True:
        print(bestword(legal_words_possible(letterdeck=user_input(),filename="C:\\Users\gbd20\Downloads\\NSWL2020.txt")))
        keepgoing = str(input("Would you like to run the program again? (Y for Yes, anything else for No)"))
        if keepgoing == 'Y':
            continue
        else:
            break

run_program()
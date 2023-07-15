

TMP = os.getenv("TMP", "/tmp")  #uses getenv (uses environemtn variales)
#in shell environment (this is an environment variable -- checking for tmp file, else default value is /tmp)


S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
#this is a url

DICT = 'dictionary.txt'
#file name

DICTIONARY = os.path.join(TMP, DICT)
#variable - this is a way to join two strings together in an agnostic

urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)
#this gets the file from a url, then stores it in a temporary directory on our local machine (caching it locally)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]


LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}



#unpack scrabble scores, the below is equivalent to LETTER_SCORES
for value, letters in scrabble_scores:
    for letter in letters.split():       #could also use str.isprint() checks truthiness of whether there is a character there
        LETTER_SCORES[letter] = value    


def load_words(text_file_path):
    '''with open(text_file_path, 'r') as file:
        words = file.read().split()
    return words'''
    return open(DICTIONARY).read().split() #this returns a list of strings This will split at ever tab, space, and newline
    

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    total = 0
    for letter in word:
        total  += LETTER_SCORES.get(letter.upper(), 0) #get the letter score the upper case letter you passed and return value, if no key then return 0
          
# total += LETTER_SCORES[letter.upper()] #actually this throws key value if you use nonnormal characters

#        or return sum(LETTER_SCORES[letter.upper()] for letter in word)

def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    max_value = 0
    highest_scoring_word = " "
    for word in words:
        value = calc_word_value(word)
        if value > max_value:
            max_value = value #this returns word with highest score
            highest_scoring_word = word
    
    return highest_scoring_word




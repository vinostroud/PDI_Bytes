import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)

def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())

print(load_dictionary())


#words = ['maamselle',
'Mabellona',
'Mabinogion',
'macaasim',
'macabresque',
'Macadamia',
'macadamite',
'macadamization',
#'racecar']
word_three = 'Aibohphobia'
word_two = 'PyBites'


#this works
def is_palindrome(word): #is_ should have hinted to return boolean
    sanitized_word = ''.join(char.lower() for char in word if char.isalnum())
    return sanitized_word == sanitized_word[::-1] #now returns true or false
  


'''tests
print(is_palindrome(word))
print(is_palindrome(word_one))
print(is_palindrome(word_two))
'''

def get_longest_palindrome(words=None):

    if words is None:
        words = list(load_dictionary())
        
    list_of_pals = []
    list_of_lengths = []
    
    for word in words:
        sanitized_word = ''.join(char.lower() for char in word if char.isalnum())
        if sanitized_word == sanitized_word[::-1]:
            list_of_pals.append(word)
        
    for palin in list_of_pals:
        #if len(i) > len(list_of_lengths[0]):
        list_of_lengths.append(len(palin))
    
    longest_palin = list_of_lengths.index(max(list_of_lengths))
    
    longest_pal_str = list_of_pals[longest_palin]

    return longest_pal_str

print(get_longest_palindrome(words))

    
    
'''
Given a list of words return the longest palindrome If called without argument use the load_dictionary helper
to populate the words list 
'''

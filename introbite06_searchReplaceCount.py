
text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

#I tried three ways to tackle this problem. All returned the same error, ImportError: cannot import name 'strip_vowels' from 'vowels' (/tmp/vowels.py)
#Also, each technique I used returned a different count?


#Approach 1 - my count is 256


count = 0
new_list=[]

def strip_vowels(text: str = TEXT) ->Tuple[str, int]:
    for letter in list(text):
        L = letter.lower()
        if L == 'a' or L == 'e' or L == 'i' or L == 'o' or L == 'u':
            new_list.append("*")
            count += 1
        else:
            new_list.append(letter)
    no_char= ""
    new_string = no_char.join(new_list)
    print(new_string, count)





#Approach 2, my count is 262

def strip_vowels(text: str = TEXT) ->Tuple[str, int]:
    count = 0
    new_text = ""

    for char in text:
        if char.lower() in "aeiou":
            new_text += "*"
            count += 1
        else:
            new_text += char

    print("New text: ", new_text)
    print("Number of replacements: ", count)





import re
from collections import Counter

def strip_vowels(text: str = TEXT) ->Tuple[str, int]:
    
    vowels = 'aeiouAEIOU'

    new_text, n_vowels = re.subn('|'.join(vowels), '*', text) #we can take advantage of `re.subn` which is the same as `re.sub` but returns a tuple. 
    #The tuple returned is the text with the replacements and a count of the number replacements made

    return new_text, n_vowels

    

    

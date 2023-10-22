import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string


    
test_string = "Hello, I am Tim."

print(remove_punctuation(test_string))
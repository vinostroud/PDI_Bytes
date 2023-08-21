

def get_profile(*,name='julian', profession='programmer'):
        return f'{name} is a {profession}'

print(get_profile())

'''
*: The asterisk * here is used to indicate that all the following parameters must be keyword-only arguments. 
Keyword-only arguments can only be passed using keyword syntax (e.g., name='Alice'), 
and they cannot be passed positionally (e.g., 'Alice').
name: This is a keyword-only parameter with a default value of 'julian'. 
If no value is provided for name, it will default to 'julian'.
profession: This is another keyword-only parameter with a default value of 'programmer'. 
If no value is provided for profession, it will default to 'programmer'.'''

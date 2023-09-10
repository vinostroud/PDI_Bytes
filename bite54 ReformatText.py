INDENTS = 4

remember_unformatted =  '''
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand

'''

Shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


def print_hanging_indents(poem):
    paragraphs = [p.strip() for p in poem.split('\n\n') if p.strip()]  # Split paragraphs, removing empty lines
    # \n\n identifies paragraphs in multiline; this is where poem is now split (split()) into paragraphs
    #'p' represents each paragraph as a string
    #strip() removes the leading and trailing whitespaces from the string
    '''by using if p.strip(), we are checking if the stripped version of the paragraph is non-empty. If a paragraph 
    contains only whitespace (empty lines), it will be considered empty and not included in the paragraphs list.
    this thusly eliminates the \n the appears at the beginning of a multiline string such as remember_unformatted'''
    #paragraphs thus is a list of each line with '\n' in betwen each line, but not at the beginning

    
    formatted_paragraphs = []

    for paragraph in paragraphs:
        lines= paragraph.split('\n') #splits paragraphs at \n, so there is now a list per paragraph
        
        cleaned_lines = [line.lstrip() for line in lines]
        #lstrip() removes spaces and tabs at the beginning of a string

        formatted_lines = [cleaned_lines[0]] #we've now created an object composed of the first line with no indent/spaces
        
        formatted_lines.extend([' ' * INDENTS + line for line in cleaned_lines[1:]])#now we add four spaces to all lines after the first line

        formatted_paragraphs.append('\n'.join(formatted_lines)) #now we add the properly formatted lines to the empty list
        
    
    formatted_text = '\n\n'.join(formatted_paragraphs) #now we've created a string, but there is a space in between the paragraphs

    formatted_text = '\n'.join(line for line in formatted_text.split('\n') if line.strip())
    #this removes empty lines from the formatted_text string. 
    #formatted_text.split('\n')creates list of lines use \n as delimiter, so each line is an element
    #'line for line...' The if line.strip() condition is used to filter out lines that are empty or 
    # contain only whitespace after stripping leading and trailing whitespace using .strip().
    #'\n'.join(...): Finally, the generator expression is joined back together into a single 
    # string using '\n' (newline) as the separator. 

    return formatted_text


print(print_hanging_indents(Shakespeare_unformatted))
#print(print_hanging_indents(remember_unformatted))

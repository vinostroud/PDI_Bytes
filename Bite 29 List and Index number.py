list_one = ['A', 'f', '.', 'Q', 2]
list_two = ['.', '{', ' ^', '%', 'a']
list_three = ['A', 'f', '.', 'Q', 2]
list_four = ['.', '{', ' ^', '%', 'a']
list_five = [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c']
list_six = ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']
list_seven = list(range(1, 9)) + ['}'] + list('abcde')
list_eight = [2, '.', ',', '!']


def get_index_different_char(chars):
        
    alpha_num = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')    
    alpha_index = []
    non_alpha_index = []


    for index_number, character in enumerate(chars):
        if character in alpha_num:
            alpha_index.append(index_number)
        else:
            non_alpha_index.append(index_number)
        
    if len(alpha_index) == 1:
        return alpha_index[0]
    else:
        return non_alpha_index[0]



#print(get_index_different_char(list_one))
#print(get_index_different_char(list_two))
print(get_index_different_char(list_three)) #2
print(get_index_different_char(list_four)) #4
print(get_index_different_char(list_five)) #1
print(get_index_different_char(list_six)) #5
print(get_index_different_char(list_seven)) #8
print(get_index_different_char(list_eight)) #0

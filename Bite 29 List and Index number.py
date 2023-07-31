'''instructions
Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:
['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
'''


list_one = ['A', 'f', '.', 'Q', 2]
list_two = ['.', '{', ' ^', '%', 'a']

list_three = ['A', 'f', '.', 'Q', 2]
list_four = ['.', '{', ' ^', '%', 'a']
list_five = [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c']
list_six = ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡']
list_seven = list(range(1, 9)) + ['}'] + list('abcde')
list_eight = [2, '.', ',', '!']


def get_index_different_char(chars):
    alpha_num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    alpha_num_iterable = [int(char) if char.isdigit() else char for char in alpha_num]    
    alpha_index = []
    non_alpha_index = []

    for index_number, character in enumerate(chars):
        if character in alpha_num_iterable:
           alpha_index.append(index_number)
        elif character not in alpha_num_iterable:
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


list = ['A', 'f', '.', 'Q', 2]




def get_index_different_char(chars):
    alpha_num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for index_number, character in enumerate(chars):
        if character not in alpha_num:
            return index_number 

print(get_index_different_char(list))
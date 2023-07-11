NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

split_names = []
list_sorted_names = []
full_sorted_names = []

for full_name in NAMES:
    split_names.append(full_name.split())
    for list_names in split_names:
        list_sorted_names.append() if 




    

    


'''
def get_lastname(name):
    return name.split()[-1]

names_titled = []


#good
def dedup_and_title_case_names(names):
    [names_titled.append(i.title()) for i in names if i.title() not in names_titled]
    return names_titled

print(dedup_and_title_case_names(NAMES))

#print(names_titled)


def sort_by_surname_desc(names):
    names_titled.sort(key=lambda name: name.split()[-1])
    return names_titled 

print(sort_by_surname_desc(NAMES))

#print(names_titled)



def shortest_first_name(names):
    names_titled.sort(key=len)
    return names_titled

print(shortest_first_name(NAMES))
'''
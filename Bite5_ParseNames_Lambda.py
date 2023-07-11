NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

names_titled = []

def dedup_and_title_case_names(names):
    [names_titled.append(i.title()) for i in names if i.title() not in names_titled]
    return names_titled
    pass

#print(dedup_and_title_case_names(NAMES))

def sort_by_surname_desc(names):
    names.sort(key=lambda name: name.split()[-1], reverse =True)
    return names
   
#print(sort_by_surname_desc(NAMES))
    # ...


def shortest_first_name(names):
    return sorted(names, key=lambda name: len(name.split()[0]))
#print(shortest_first_name(NAMES)) 
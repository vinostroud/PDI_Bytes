NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
    return [name.title() for name in set(names)]

def sort_by_surname_desc(names):
    deduped_names = dedup_and_title_case_names(names)
    return sorted(deduped_names, key=lambda name: name.split()[-1], reverse=True)
 
def shortest_first_name(names):
    
    deduped_names = dedup_and_title_case_names(names)
    shorted_first_name_list = sorted(deduped_names, key=lambda name: len(name.split()[0]))
    shortest_full_name = shorted_first_name_list[0].split()

    return (shortest_full_name[0])

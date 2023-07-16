names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()



def enumerate_names_countries():
    results = ''
    for index, (name, country) in enumerate(zip(names, countries), 1):
        results += f'{index}. {name:<10} {country:<11}\n'
    return results

print(enumerate_names_countries()) 




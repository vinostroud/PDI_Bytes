names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()



def enumerate_names_countries():
    results = ''
    for index, (name, country) in enumerate(zip(names, countries), 1):
        results += f'{index}. {name:<10} {country}\n' #sets second column as width 11, < let justifies it
    #print(repr(results))  <<used this for debugging
    print(results, end="")  #print(  end) was needed so that the program did not create a newline, failing the test

print(enumerate_names_countries())  




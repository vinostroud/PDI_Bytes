from collections import Counter, namedtuple
import os
import urllib.request

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = ['static', 'templates', 'data', 'pybites', 'bbelderbos', 'hobojoe1848']

Stats = namedtuple('Stats', 'user challenge')


# code


def gen_files(tempfile=tempfile):
    with open (tempfile) as file:
        for line in file.readlines():
            line = line.strip() #strip removes white space from left and right hand sides of string           
            file_or_dir, is_dir = line.split(',') #this unpacks the list that line.split creates into the tuple 
            if is_dir.lower() == 'true':
                yield file_or_dir.lower()

#NOTES on the above
#looking at file, false != directory, True = is a directory
#Go through list of things, looking for a directories. We know is a directory based on Ture
#therefore we can split [or strip] the line on the comma 


def diehard_pybites(files=None):

    if files is None:
        files = gen_files()

    users = Counter()
    popular_challenges = Counter()

    list_of_numbers = []
    list_of_names = []

    for combined_text in files:
        split_text = combined_text.strip()
        number, user_name = split_text.split('/')
        
        if user_name not in IGNORE:
            list_of_numbers.append(number)
            list_of_names.append(user_name)

    total_number_numbers = Counter(list_of_numbers)
    total_number_names = Counter(list_of_names)
        
    most_common_user = total_number_names.most_common(1)[0][0]
    most_common_challenge = total_number_numbers.most_common(1)[0]

    return Stats(user=most_common_user, challenge=most_common_challenge)

'''
total_number_names.most_common(1): This part of the expression calls the most_common method of the Counter object total_number_names. The most_common method returns a list of tuples representing the elements in the Counter with their counts, sorted in descending order. The argument 1 specifies that we want the most common element (top element) along with its count. The return value is a list containing one tuple.

[0]: After calling most_common(1), we have a list with a single tuple. Using [0] on this list extracts the first (and only) element, which is the most common element with its count. Since there is only one element, this step is necessary to access the tuple inside the list.

[0]: Finally, we use [0] again on the tuple to access the first element of the tuple, which is the most common element itself. In this case, the most common element is the user with the highest count.

So, total_number_names.most_common(1)[0][0] gives us the most common user (the username) based on the counts obtained from the Counter object total_number_names.

The same logic applies to total_number_numbers.most_common(1)[0]. It retrieves the most common challenge and its count as a tuple from the Counter object total_number_numbers. The tuple contains two elements: the challenge and its count, but we are only interested in the challenge, so we access it using [0].






'''

        
print(diehard_pybites(files=[
            "22/wonderfulboyx",
            "25/bbelderbos",  # ignored
            "25/clamytoe",
            "21/wonderfulboyx",
            "25/santiagobenitez",
            "23/santiagobenitez",
            "07/santiagobenitez"
        ]))


"""Notes on above
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """

 

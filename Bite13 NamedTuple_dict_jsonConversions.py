
from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
BlogEntry = namedtuple('BlogEntry', blog.keys()) #namedtuple gets field names the return the keys (blog.keys())


def dict2nt(dict_):
    nt = BlogEntry(**dict_) #unpacking the dictionary into the named tuple's constructor using the **dict_ 
    return nt

#print(dict2nt(blog))
'''Just FYI Modify a named tuple field
nt = nt._replace(name='NewPyBites')
'''

def nt2json(nt):
    nt = dict2nt(blog)
    return json.dumps(nt._asdict(), default=str)

'''
Notes:
nt._asdict(): The _asdict() method is a method provided by named tuples that converts the named tuple into an ordered dictionary. 
An ordered dictionary is similar to a regular dictionary, but it preserves the order of insertion of key-value pairs. 
This method returns a dictionary where the keys are the field names of the named tuple and the values are the corresponding field values.

json.dumps(...): The json.dumps() function is part of the json module in Python and is used to convert Python objects into JSON-formatted strings.

default=str: This is an optional argument for json.dumps() that specifies a function to be called for objects that are 
not serializable by the default JSON encoder. In this case, we're using str as the function to convert any non-serializable values 
to their string representation. The default argument is applied to values that cannot be directly serialized by JSON, 
such as datetime objects. By default, Python's str() function is used to convert these objects to strings, making them serializable.

In sum: 
Converting the named tuple nt to an ordered dictionary using nt._asdict().
Serializing the ordered dictionary into a JSON-formatted string using json.dumps().
For values that cannot be directly serialized (such as datetime objects), converting them to strings using the str() function before serializing.
This process results in a JSON-formatted string that represents the named tuple's data in a JSON-compatible format.
'''
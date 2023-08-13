
User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here

class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass


def get_secret_token(username):
    try:
        user = next(user for user in USERS if user.name == username) #next() function is used to retrieve the next value from an iterable.
        #This iterates through each User object in the USERS tuple and filters out those whose name attribute matches the given username.
        if user.expired:
            raise UserAccessExpired('Token Expired')  #user.expired is referencing an attribute of the User namedtuple (dot notation)
        elif user.role == ADMIN:
            return SECRET
        else:
            raise UserNoPermission('Not permitted')
    except StopIteration:
        raise UserDoesNotExist('No username')     
              
           






'''
a function that takes a username and checks for a valid user:

1. The username is in USERS

2. The user's account has not expired.

3. The user has the ADMIN role.

If those 3 conditions are met return SECRET.

If one of the conditions is not True, raise an appropriate exception:

- UserDoesNotExist

- UserAccessExpired

- UserNoPermission
'''

'''
Tests:
#1
from validate import (get_secret_token, SECRET,
                      UserDoesNotExist, UserAccessExpired, UserNoPermission)

#2
def test_get_secret_token():
    assert issubclass(UserDoesNotExist, Exception)
    assert issubclass(UserAccessExpired, Exception)
    assert issubclass(UserNoPermission, Exception)

    with pytest.raises(UserDoesNotExist):
        get_secret_token('Tim')
    with pytest.raises(UserAccessExpired):
        get_secret_token('Bob')
    with pytest.raises(UserNoPermission):
        get_secret_token('Julian')

        
#3
    assert get_secret_token('PyBites') == SECRET
'''
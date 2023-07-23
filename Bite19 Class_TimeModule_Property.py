from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(expires, datetime):
            raise TypeError("Expires must be a datetime object.")
        self.name = name
        self.expires = expires
    
    @property
    def expired(self):
        current_time = datetime.now()
        return self.expires < current_time
    
'''
Assignment:
Write a simple Promo class. Its constructor receives two variables: name 
(which must be a string) and expires (which must be a datetime object).

Add a property called expired which returns a boolean value indicating 
whether the promo has expired or not.
'''
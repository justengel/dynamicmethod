#Dynamic class and instance methods!
This simple module creates a class method that will also work as an instance method.

```python
import dynamicmethod

class Example(object):

    x = 1  # Default classmethod value

    def __init__(self, x=0):
        self.x = x

    @dynamicmethod
    def get_x(self):
        return self.x
        
print(Example.get_x())
ex = Example()
print(ex.get_x())
ex.x = 5
print(ex.get_x())
```

I have grown to use this module quite a bit. Mostly I make a default class level dictionary where each instance 
can be customized.

```python
from dynamicmethod import dynamicmethod

class Lookup(object):

    lookup_type = {'type1': 1, 'mytype2': 2}
    
    def __init__(self):
        # Save an instance variable so the class variable does not change.
        self.lookup_type = self.__class__.lookup_type.copy()
        
    @dynamicmethod
    def add_type(self, name, value):
        self.lookup_type[name] = value
        
    @dynamicmethod
    def get_type(self, name):
        return self.lookup_type.get(name, None)
        

Lookup.add_type('New Type', 3)
print(Lookup.get_type('New Type'))

specific_lookup = Lookup()
print(specific_lookup.get_type('New Type'))

specific_lookup.add_type('hello', 'world!')
print(specific_lookup.get_type('hello'))
# print(Lookup.get_type('hello'))  # This would be None since the class lookup does not contain 'hello'
```

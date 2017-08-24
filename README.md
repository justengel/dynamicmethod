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

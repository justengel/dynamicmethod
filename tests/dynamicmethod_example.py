import dynamicmethod


class Example(object):

    x = 0  # Default classmethod value

    def __init__(self, x=0):
        self.x = x

    @dynamicmethod
    def get_x(self):
        return self.x

print(Example.get_x())
ex = Example(1)
print(ex.get_x())
ex.x = 5
print(ex.get_x())



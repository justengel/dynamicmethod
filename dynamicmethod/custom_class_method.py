"""
Class decorator that can also use instance values.

Example:

        ..code-block :: python

            >>> import dynamicmethod
            >>> class Example(object):
            >>>     x = 0
            >>>
            >>>     def __init__(self, x=0):
            >>>         self.x = x
            >>>
            >>>     @dynamicmethod
            >>>     def get_x(self):
            >>>         return self.x
            >>>
            >>> print(Example.get_x())
            >>> ex = Example()
            >>> ex.x = 5
            >>> print(ex.get_x())

"""


class dynamicmethod(classmethod):
    """Decorator to create a class method that will also be an instance method."""
    def __get__(self, inst, typ):
        if inst is not None:
            # Instance method
            bound_method = self.__func__.__get__(inst, inst.__class__)
            return bound_method

        # Class method
        return super().__get__(inst, typ)


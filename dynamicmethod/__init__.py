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

from .__meta__ import version as __version__

import sys


__all__ = ['__version__', 'dynamicmethod']


class dynamicmethod(object):
    """Decorator to create a class method that will also be an instance method."""
    def __init__(self, func):
        self.__func__ = func

    def __get__(self, inst, cls):
        if inst is not None:
            # Instance method
            bound_method = self.__func__.__get__(inst, cls)
            return bound_method
        else:
            # Class method
            return self.__func__.__get__(cls, cls)


MY_MODULE = sys.modules[__name__]


class DynamicModule(MY_MODULE.__class__):
    def __call__(self, function):
        """Decorator to create a class method that will also be an instance method.

        Example:

            ..code-block :: python

                >>> from dynamicmethod import dynamicmethod  # or just "import dynamicmethod"
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
        return dynamicmethod(function)


# Override the module make it callable
try:
    MY_MODULE.__class__ = DynamicModule  # Override __class__ (Python 3.6+)
    MY_MODULE.__doc__ = DynamicModule.__call__.__doc__
except (TypeError, Exception):
    # < Python 3.6 Create the module and make the attributes accessible
    sys.modules[__name__] = MY_MODULE = DynamicModule(__name__)
    for ATTR in __all__:
        setattr(MY_MODULE, ATTR, vars()[ATTR])

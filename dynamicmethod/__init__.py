from .__meta__ import version as __version__

import sys
import types
from .custom_class_method import dynamicmethod


class DynamicModule(types.ModuleType):
    """Custom callable module.

    This can be called by the following example.

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

    This class module is implemented so you don't have to call
    ..code-block :: python

        >>> import dynamicmethod
        >>> dynamicmethod.dynamicmethod

    """
    __version__ = __version__

    dynamicmethod = dynamicmethod

    def __call__(self, function):
        return self.dynamicmethod(function)


# Make this module callable
sys.modules[__name__] = DynamicModule(__name__)

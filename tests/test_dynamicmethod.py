

def test_dynamicmethod():
    import dynamicmethod

    class Example(object):

        x = 0  # Default classmethod value
        y = 0  # Default classmethod value

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        @dynamicmethod
        def get_x(self):
            return self.x

        @dynamicmethod
        def get_y(self):
            return self.y

    assert Example.get_x() == 0, "Basic class method failed!"
    assert Example.get_y() == 0, "Basic class method failed!"

    myexample = Example()
    assert myexample.get_x() == 0, "Basic instance method failed!"
    assert myexample.get_y() == 0, "Basic instance method failed!"

    Example.x = 1
    Example.y = 1

    assert Example.get_x() == 1, "Changed value class method failed!"
    assert Example.get_y() == 1, "Changed value class method failed!"

    # Make sure init sets the instance value
    assert myexample.get_x() == 0, "Basic instance method failed!"
    assert myexample.get_y() == 0, "Basic instance method failed!"

    myexample.x = 2
    myexample.y = 2

    assert myexample.get_x() == 2, "Basic instance method failed!"
    assert myexample.get_y() == 2, "Basic instance method failed!"

    assert Example.get_x() == 1, "Changed value class method failed!"
    assert Example.get_y() == 1, "Changed value class method failed!"


def test_no_init_values():
    """Test if init does not set the initial value for the instance."""
    import dynamicmethod

    class Example(object):

        x = 0  # Default classmethod value
        y = 0  # Default classmethod value

        @dynamicmethod
        def get_x(self):
            return self.x

        @dynamicmethod
        def get_y(self):
            return self.y

    assert Example.get_x() == 0, "Basic class method failed!"
    assert Example.get_y() == 0, "Basic class method failed!"

    myexample = Example()
    assert myexample.get_x() == 0, "Basic instance method failed!"
    assert myexample.get_y() == 0, "Basic instance method failed!"

    Example.x = 1
    Example.y = 1

    assert Example.get_x() == 1, "Changed value class method failed!"
    assert Example.get_y() == 1, "Changed value class method failed!"

    # The values are the same as the class method
    assert myexample.get_x() == 1, "Basic instance method failed!"
    assert myexample.get_y() == 1, "Basic instance method failed!"

    myexample.x = 2
    myexample.y = 2

    assert myexample.get_x() == 2, "Basic instance method failed!"
    assert myexample.get_y() == 2, "Basic instance method failed!"

    assert Example.get_x() == 1, "Changed value class method failed!"
    assert Example.get_y() == 1, "Changed value class method failed!"

import functools

from .my_class import MyClass

class RegisterMethod():
    """Register a method to MyClass as a plug-in.

    Usage::

        from .register_method import RegisterMethod

        @RegisterMethod
        def hello_wordl(self, name):
            return f"Hello world from Doctor {name}"

    Then, 

        MyClass().hello_world("Who")
          # => "Hello world from Doctor Who"
    """

    def __init__(self, func):
        functools.update_wrapper(self, func)
        setattr(MyClass, func.__name__, func)


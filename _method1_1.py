from .register_method import RegisterMethod # Or remove "." if NOT in a package.
from .my_class import MyClass               # Or remove "." if NOT in a package.

@RegisterMethod
def my_method1_1(self, *arg, *opts):        # With no prefix of an underscore.
    pass

@RegisterMethod
def my_method1_2(self, *arg, *opts):        # With no prefix of an underscore.
    pass


def my_local_method1(self, *arg, *opts):    # Method valid only in this file.
    pass

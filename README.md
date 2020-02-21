

Decorator to add a method to an existing class
==============================================

This repo contains a group of files to add (or register) a method to an existing class.  Here it is assumed, for the sake of demonstration, that

* Everything is in a package.
  * If your case is not, adjust the import statement accordingly.
* The name of the existing class is `MyClass` defined in `my_class.py`
* The methods to add to `MyClass` are `my_method1_1` and alike and are defined in `_my_method1.py`.
  * This file can contain
    1.  an arbitrary number of methods that are meant to be registered, 
    2.  an arbitrary number of local methods that are valid only in the file `_my_method1.py` (unless they are explicitly imported by some external programs)
  * An arbitrary number of similar files to define methods can be created.
* The name of the decorator is `RegisterDef` defined in `register_def.py` 

Providing a method will have been loaded by the time it is called from `MyClass`, the method call from MyClass is stated as normal (e.g., `self.my_method1_1(*args, **opts)` in the original definition of `MyClass`.  If you need to call one dynamically, the statement is like:

```python
class MyClass():

    # As an instance method
    self.__getattribute__(method)(*args, **opts)
   
    # To call it (that defined as an instance method) as a class method
    cls = self.__class__  # Or inside a @classmethod
    cls.__getattribute__(cls, method)(*args, **opts)
```

## Other ways to achive ##

Here are other ways to achive "registering a method to an existing file".

### Without a decorator ###

Basically, do the same thing manually without using a decorator:

```python
# in _my_method1.py
def my_method1_1(self):
    return

m = my_method1_1
setattr(MyClass, m.__name__, m)
```

### Use `import` inside the class ###

Taken from [an answer in StackOverflow](https://stackoverflow.com/questions/47561840/python-how-can-i-separate-functions-of-class-into-multiple-files/47562412#47562412)

```python
# Maybe in __init__.py
class MyClass():
    # Importing methods
    from ._my_method1 import my_method1_1  # To dynamically load ``def``
    from ._my_method1 import my_method1_2

    def __init__(): pass  # or whatever small functions.
```

### Wrap them in mixin classes ###

In `my_class.py`

```python
from ._mixin_class1 import MixinClass1
from ._mixin_class2 import MixinClass2
class MyClass(MixinClass2, MixinClass1):
    ...
    pass
```

In `_mixin_class1.py`:

```python
# In a separate file (the filename may be prefiwed with "_"
class MixinClass1():
    def my_metho1_1(): pass

    @classmethod
    def my_classmetho1_2(): pass
```

### Put them in child classes ###

If the methods are not instance methods, but class or static methods, the following would work, too.

```python
class MyChild1(MyClass):
    # Define a single method (run(), for example) per class?
    @classmethod
    def run(cls, *arg, **opts): pass
```

And once it is loaded, MyClass can find its subclasses. If you want the list of their String names:

```python
classes = [i.__name__ for i in MyClass.__subclasses__()]  # list(name_string)
```

Then, you can run it like:

```python
for em in MyClass.__subclasses__():
    em.run(*arg, **opts)
```


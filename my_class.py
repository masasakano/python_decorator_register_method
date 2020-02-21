class MyClass():
   def __init__():
       pass

   def a_method(self, methodname: str, *arg, **opts):
       # If you know the method name.
       self.my_method1_1(methodname, *arg, **opts)

       # to call one dynamically:
       self.__getattribute__(methodname)(*args, **opts)

       # to call one dynamically as a class method:
       cls = self.__class__
       cls.__getattribute__(cls, methodname)(*args, **opts)


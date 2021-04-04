# abc_combinded_with_static_property

*```@abstractmethod``` only validates the presence of an attribute with the given name in a inherited class, not the type of that attribute* 

The ```@abstractmethod``` parameter only checks that the name is mapped to the child class.

It can be stacked with ```@staticmethod``` or ```@property``` unfortunately it does no checking that the sub class implements the name as a ```@staticmethod``` or ```@property```

Example with staticmethod:

```python

class ContractInterface(ABC):
    @staticmethod
    @abstractmethod
    def should_be_static():
        pass


class ImplementationDetails(ContractInterface):
    def should_be_static(self):
        print("This is not static")


class ImplementationIgnoringInterface(ContractInterface):
    @staticmethod
    def not_using_interface():
        print("Ignoring interface without TypeError")

'''
prints "This is not static" when this 
ideally would throw a TypeError when run
'''
ImplementationDetails().should_be_static()

'''
prints "Ignoring interface without TypeError" when this 
ideally would throw a TypeError when run
'''
ImplementationIgnoringInterface.not_using_interface()
```




Example with property:

```python

class ContractInterface(ABC):
    @property
    @abstractmethod
    def should_be_static():
        pass


class ImplementationDetails(ContractInterface):
    def should_be_static(self):
        print("This is not static")


class ImplementationIgnoringInterface(ContractInterface):
    @staticmethod
    def not_using_interface():
        print("Ignoring interface without TypeError")

'''
prints "This is not static" when this 
ideally would throw a TypeError when run
'''
ImplementationDetails().should_be_static()

'''
prints "Ignoring interface without TypeError" when this 
ideally would throw a TypeError when run
'''
ImplementationIgnoringInterface.not_using_interface()
```
# abc_combinded_with_static_property

*```@abstractmethod``` only validates the presence of an attribute with the given name in a inherited class, not the type of that attribute* 

The ```@abstractmethod``` parameter only checks that the name is mapped to the child class.

It can be stacked with ```@staticmethod``` or ```@property``` unfortunately it does no checking that the sub class implements the name as a ```@staticmethod``` or ```@property```

Example with staticmethod:

```python

from abc import ABC
from abc import abstractmethod

class ContractInterface(ABC):
    @staticmethod
    @abstractmethod
    def should_be_static():
        pass


class ImplementationInterface(ContractInterface):
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
ImplementationInterface().should_be_static()

'''
prints "Ignoring interface without TypeError" when this 
ideally would throw a TypeError when run
'''
ImplementationIgnoringInterface.not_using_interface()
```




Example with property:

```python
from abc import ABC
from abc import abstractmethod

class ContractValueObject(ABC):
    @property
    @abstractmethod
    def important_data(self):
        pass


class ImplementationValueObject(ContractValueObject):
    def important_data(self):
        print("This is not a property")


'''
prints "This is not a property" when this 
ideally would throw a TypeError when run
'''
ImplementationValueObject().important_data()


```
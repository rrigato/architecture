# abc_combinded_with_static_property
The ```@abstractmethod``` parameter only checks that the name is mapped to the child class.

It can be stacked with ```@staticmethod``` or ```@property``` unfortunately it does no checking that the sub class implements the name as a ```@staticmethod``` or ```@property```

Example:

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
    def not_using_interface(self):
        print("This is not static")

'''
prints "This is not static" when this would throw a 
TypeError when run
'''
ImplementationDetails().should_be_static()
```
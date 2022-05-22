all - all items of an iterable are True
any - any item in the iterable is True

@classmethod signifies that a function can be invoked on a the class or an instance of the class, receives an implicit first argument ```cls``` shared across all instances

dir(<object_name>) provides all objects in the current context or the objects attached to the object provided as an argument 
vars(<an_object>)  returns the __dict__ attribute 

filter(<function>, <iterable>) returns an iterable with all elements in <iterable> where <function> returns True

getattr raises an AttributeError if the attribute passed does not exist on the object


isinstance(<potential_instance>, <object_type>)


map(<function_name>, <iterable>) = returns an iterable where <function_name> was run on every element of the <iterable>


@property = defines getters, setters and deleters for an attribute on a property

@staticmethod function that can be invoked on an instance or the object, does not have an implicit cls object

- reversed(<sequence>) = returns an iterable that is the reverse of sequence

sorted(<an_iterable>) returns a sorted list from the iterable, you can provide a function to create a custom key


Recommends isinstance for object type comparisons

zip(<iterators>) returns an iteratable where the ith element is a tuple containing the ith elements of all <iterators> passed as arguements


```python 
for idx, value enumerate(["a", "b", "c"]):
    '''
        iterator of the following
        [(0, "a"), (1, "b"), (2, "c")]
    '''
```


```python 

print({}.get("a")) # None

new_dict = {"a": "value"}

print(new_dict.setdefault("b", "new_value")) # "new_value"
print(new_dict.setdefault("a", "old_value")) # "value"
print(new_dict) # {"a": "value", "b": "new_value"} 
```




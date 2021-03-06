# Immutable me

This week, we are going to explore the idea of immutability, and what it takes to make a data structure both immutable and flexible enough for real use.

The idea of an immutable type is that you can set its value when the object is created, but cannot change it afterwards. Think of strings and tuples, and I think you'll understand the point.

What I want you to do is create a class, `ImmutableParent`. This class is basically an abstract base class (but you don't have to define it explicitly as such). The idea is that other classes will inherit from it. When a class inherits from `ImmutableParent`, they should **not** implement `__init__` on their own. Instead, `__init__` will take `**kwargs`, and will use the key-value pairs there to set attributes on the object.

Any attempt to change an attribute's value, or to add a new attribute, will result in an exception being thrown. For example:

```python
im = ImmutableMe(x=111,y=222,z=333)
print(f'Before, vars(im) = {vars(im)}')    # shows x=111, y=222, z=333
im.x = 999            # exception thrown; cannot change an attribute
im.a = 'Hello'        # exception thrown; cannot add an attribute
```

Note that if an attribute is itself mutable, then its contents may be changed.

There are a few ways to solve this, but I don't want you to use a named tuple for this.

The code needs to pass the tests in [ex39_immutable_me_test.py](ex39_immutable_me_test.py) file.

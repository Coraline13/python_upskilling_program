# str_range

One of the things that I like about the Ruby programming language is that it has a `Range` class. Ruby's `Range` objects operate similarly to the output from Python's `range` function, except that they work on more than just numbers. For example, in Ruby, I can iterate over the letters from 'm' to 'z' without having to specify them explicitly.

This week, we're going to create an iterator called `str_range` that will implement just that: you'll call `str_range` similarly to how you call the built-in `range` function: with a starting value, an ending value, and an optional step value. Note that you cannot imply the start of a string range, so the first two parameters are mandatory. Also, as opposed to Python's numeric ranges, these will be up to and including the final point.

For example, if you invoke `str_range('j', 'm')`, you'll get a generator back that produces each of the letters of another's book.

Moreover, because we're using Python 3, it should be possible for the starting and ending characters to be in a non-Latin (or even non-alphabetic) script, although in such languages, the idea of "iterating over all characters" doesn't quite exist, and might end up giving you a very, very long series of outputs.

For example, here are three calls to our generator:
```python
for letter in str_range('j', 'p'):
    print(letter, end=' ')
print('\n')

for letter in str_range('א', 'ז'):
    print(letter, end=' ')
print('\n')

for letter in str_range('א', 'ז', 2):
    print(letter, end=' ')
print('\n')
```


Here is the output from these runs:
```
j k l m n o p

א ב ג ד ה ו ז

א ג ה ז
```

Note that the final two are the first seven and the 1st, 3rd, 5th, and 7th letters of the Hebrew alphabet. (They might not appear in the correct order on your screen.)

The code needs to pass the tests in [ex23_str_range_test.py](ex23_str_range_test.py) file.

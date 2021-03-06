# loglistclass

Last week, we wrote a function that turns a logfile into a list of dicts. This week, we'll use what we did, turning it into a class from which we can retrieve information about that logfile.

At the heart of this class will be the same list of dicts. That is, when we create an instance of our `LogDicts` class, we'll load the entire file into memory (you can assume that the logfile isn't too big; perhaps in the future, we'll talk about "chunking" files that are too load to read all at once). Then, with that in place, we'll be able to invoke a number of different methods:

```python
ld = LogDicts('mini-access-log.txt')
```

Again, creating an instance of `LogDicts` will load the list of dicts into the object, making them available for our use.

```python
ld.dicts(key=None)      # return the list of dicts, same as last week's exercise
ld.iterdicts(key=None)  # returns an iterator of dicts, rather than the list all at once

ld.earliest()   # returns the dict with the earliest timestamp
ld.latest()     # returns the dict with the latest timestamp
```

In order for these two methods to work, you'll need to turn the timestamp into an actual time object. I'd suggest using `time.strptime`, although there are alternatives on PyPI that you might prefer, such as `arrow`.

```python
ld.for_ip(ip_address, key=None)   # returns all records for a particular IP address
ld.for_request(text, key=None)    # returns all records whose request contains text
```

The above will return a subset of the list, filtering for certain IP addresses and text. The text can be a plain ol' string. You don't have to use a regexp, unless you want to do so, of course.

If you're wondering why `ld.dicts`, `ld.iterdicts`, and `for_ip` all take a `key` parameter, it's because we want our users to be able to sort the resulting list of dictionaries. For example, I should be able to say:

```python
def by_ip_address(one_log_dict):
    return one_log_dict['ip_address']

ld.dicts(key=by_ip_address)
```

The function can be a lot more complex than this, if we want. But it's nice to be able to sort the results according to something we want, such as, for example, the path of the request.

The code needs to pass the tests in [ex4_loglistclass_test.py](ex4_loglistclass_test.py) file.

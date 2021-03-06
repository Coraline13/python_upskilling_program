# File info class

Last week, we created a program that creates a list of dictionaries. Each dictionary contained information (path, timestamp, and SHA-1 digest) for a file.

Now, it's totally acceptable to use lists of dictionaries. But it's often easier and better to work with objects.

This week, I thus want you to create a `FileList` class, which will contain any number of `FileInfo` objects. The `FileInfo` objects will be the class equivalent of our dictionaries, with three attributes instead of three name-value pairs. The `FileList` class will not only contain the list of files, but will also contain the timestamp indicating when we last collected data about our files. It'll also contain the directory whose contents we're tracking.

In other words: last week, our program created a list of dicts. Now we're going to create a single `FileList` instance, containing any number of `FileInfo` objects, as well as a timestamp and directory name.

In addition to creating the class, we'll also need a bit of additional functionality.

First, I want you to implement a `rescan` method on the `FileList`. This will go through the named directory, adding any files that have been added since the first scan, removing any that have been removed, and indicating which files (if any) have changed since the last scan (i.e., whose SHA-1 has changed). The `rescan` method should return a dictionary when done The keys of the dictionary will be `added` (a list of filenames that have been added), `removed` (a list of filenames that have been removed), and `changed` (a list of filenames whose SHA-1 differs from that on disk). Files that haven't changed won't be included in this `rescan` output.

Second, I want you to ensure that you can store an instance of `FileList` to disk using `pickle`. And of course, that you can retrieve the `FileList` instance from disk using the `load` function from the `pickle` module, too.

The code needs to pass the tests in [ex26_file_info_class_test.py](ex26_file_info_class_test.py) file.

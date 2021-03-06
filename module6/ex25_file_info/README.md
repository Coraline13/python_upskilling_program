# File info

This week, we're going to start to work on a small application that detects whether files have been changed or otherwise tampered with. The aim here isn't to compete with such systems as Tripwire, but rather to work a bit with hashing, data storage, and reporting.

This exercise will extend over several weeks. This week, we'll start the process by writing a program that collects information about files, and creates a data structure from that information.

In other words: you should write a function, `get_file_info`, that takes a single argument, `pathname`, the name of a directory. The program will then go through each of the files in that directory, as well as in any subdirectories, and will calculate the SHA-1 of that file.

The program should then produce (and print) a data structure — a list of dictionaries — in which each dictionary will contain the following information:
- full path and filename
- file timestamp
- SHA-1 of the file's contents

This exercise combines a number of different things:
- the use of `os.walk` to go through an entire directory/tree structure
- the use of `os.stat` to retrieve information about files
- the calculation of a hash function (SHA-1, in this case) on a file's contents

The code needs to pass the tests in [ex25_file_info_test.py](ex25_file_info_test.py) file.

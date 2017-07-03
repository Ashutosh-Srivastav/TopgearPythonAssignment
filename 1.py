>>> mylist = range(4)
>>> seclist = mylist
>>> print seclist
Output: [0, 1, 2, 3]
>>> mylist.append(4)
>>> print seclist
Output: [0, 1, 2, 3, 4]
>>> seclist = mylist[:]
>>> print seclist
Output: [0, 1, 2, 3, 4]
>>> mylist.append(5)
>>> print seclist
Output: [0, 1, 2, 3, 4]


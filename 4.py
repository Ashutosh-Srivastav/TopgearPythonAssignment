>>> counter = 1
>>> def dolots(count):
...   global counter
...   for i in (1, 2, 3):
...     counter = count + i
... 
>>> print dolots(4)
Output: None
>>> print counter
Output: 7


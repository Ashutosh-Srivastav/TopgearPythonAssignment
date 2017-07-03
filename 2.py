#Output of Question 2:

>>> def f(n):
	for x in range(n):
		yield x**3


>>> for x in f(6):
	print(x)


0
1
8
27
64
125

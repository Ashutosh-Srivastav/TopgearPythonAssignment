'''Question
6. Create 3 Lists ( list1,list2,list3) with numbers and perform following operations
         a) Create Maxlist by taking 2 maximum elements from each list.
         b) Find average value from all the elements of Maxlist.
         c) Create a MinlIst by taking 2 minimum elements from each list
         d) Find the average value from all the elements of Minlist
Question'''
#program
l1= [12,13,45,65,33,22,43,44,23,47]
l2= [2,3,4,3,2,455,6,4,3,23,4,53,43]
l3= [23,4,54,3,45,5,45,3,3,5,65,4,3,55]
l1.sort()
l2.sort()
l3.sort()
maxlist=[]
minlist=[]
for i in (l1,l2,l3):
    maxlist.append(i[-1])
    maxlist.append(i[-2])
print ('maxlist is: '+repr(maxlist))
print('Average of maxlist= '+repr(sum(maxlist)/len(maxlist)))
for i in (l1,l2,l3):
    minlist.append(i[0])
    minlist.append(i[1])
print ('minlist is: '+repr(minlist))
print('Average of minlist = '+repr(sum(minlist)/len(minlist)))

'''Solution
osgdev@DHZ-PES03:~/Python_as338011/PythonL1Assignment$ python 6.py
maxlist is: [65, 47, 455, 53, 65, 55]
Average of maxlist= 123
minlist is: [12, 13, 2, 2, 3, 3]
Average of minlist = 5
Solution'''

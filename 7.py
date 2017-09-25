'''Question
7. Write program to convert prefix/net mask to IP
eg: input:16  output: 255.255.0.0
Question'''

#program
number=int(input("Enter a number between 0 and 32 to convert it to masked IP: "))
l=number/8
m=number%8
block1=block2=block3=block4=0
def fn(x):
    if x==1:
        return 128
    if x==2:
        return 192
    if x==3:
        return 224
    if x==4:
        return 240
    if x==5:
        return 248
    if x==6:
        return 252
    if x==7:
        return 254
if l==0:
    block1=fn(m)
if l==1:
    block1=255
    block2=fn(m)
if l==2:
    block1=255
    block2=255
    block3=fn(m)
if l==3:
    block1=255
    block2=255
    block3=255
    block4=fn(m)
if l==4:
    block1=255
    block2=255
    block3=255
    block4=255
print("{block1}.{block2}.{block3}.{block4}".format(**locals()))

'''Solution
Enter a number between 0 and 32 to convert it to masked IP: 21
21
255.255.248.0
osgdev@DHZ-PES03:~/Python_as338011/PythonL1Assignment$ python 7.py
Enter a number between 0 and 32 to convert it to masked IP: 11
255.224.0.0
osgdev@DHZ-PES03:~/Python_as338011/PythonL1Assignment$ python 7.py
Enter a number between 0 and 32 to convert it to masked IP: 29
255.255.255.248
Solution'''

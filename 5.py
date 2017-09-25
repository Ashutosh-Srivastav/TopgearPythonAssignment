'''Question
5. Write a code to read  the data from  input file called input.txt and count the number of characters per line,
 number of words per line and write these into output file called as output.txt

Question'''

#program
file=open('FiletoReadfor5.py.txt',"r")
filestr=file.read()
lengthoffile=len(filestr)
print (lengthoffile)
listoflines=filestr.split('\n')
numberoflines=len(listoflines)
for i in range(0,numberoflines):
    print(len(listoflines[i]))


'''Output
osgdev@DHZ-PES03:~/Python_as338011/PythonL1Assignment$ python 5.py
130
11
23
57
35
Output'''

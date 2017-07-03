'''Question
3. Write a program to receive a string from keybord and check if the string has two 'e' in the characters.
   If yes return True else False.
Question'''

#Program

str1=input("Enter a string : ")
count=0
strlen=len(str1)
for i in range(0,strlen):
    if (str1[i]=='e'):
        count=count+1
if count>1:
	print ("True")
else:
    print("False")


'''Output:
osgdev@DHZ-PES03:~/Python_as338011/PythonL1Assignment$ python 3.py
Enter a string : "Hello World"
False
osgdev@DHZ-PES03:~/Python_as338011/PythonL1Assignment$ python 3.py
Enter a string : "Hellee"
True
Output'''

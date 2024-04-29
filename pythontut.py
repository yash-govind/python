# test_1=int(input("enter kro : "))
# test_2=int(input("Enter karo again : "))
# sum=print(test_1+test_2)
# # default string jaise leta hai
# test1=(input("Enter a number\" : "))
# test2= input("Enter another number : ")
# sum=print("Here is the result of conatination of strings : ",test1+test2)

#looping through strings : 

# str1="hi"
# str2="hellow"
# for character in str2:
#     print(character)
    
#accessing characters in a string : 

# str1="hi"
# print(str1[1])

#multiline strings : 
# str1="""hi how are yu im goodd
#    tum kaise ho bhai hum bhi badiya 
#    i am also good"""
# print(str1)

# string slicing and methods.

# str1="YASH"
# print(str1[0:3]) # prints from 0 th index to 3-1=2 th index.
# print(len(str1)) #gets the length of string which is 4
# print(str1[-3 :-1]) # its the same as ((len(str1)-3) : len(str1)-1))=(str1[1 : 3]) which prints from 1st index to 2nd index

#string methods : 
# str1="YASH &&& **!!! abcdefghijklmnopqrstuvwxyz"
# print(str1.upper()) # converts string to uppercase
# print(str1.lower()) #converts string to lowercase
# print(str1.rstrip("!")) #removes last ke ! characters.
# print(str1.replace("YASH","PERSON_X")) #replaces string YASH with string PERSON_X
# print(str1.split(" ")) # makes a  sub-string into a list wherever space is present .
# print(str1.capitalize()) #makes first character capital and rest of characters into lowercase
# print(str1.center(120)) # adds 120 spaces before the string and aligns the string to centre 
# print(str1.count("y")) # counts the number of times the character "y"(capital and small) has occured
# print(str1.endswith("z")) #tells us character the string is ending with . spaces are also included.
# print(str1.endswith("i",1,5))#we can also check for a character which in a range of indexes
# print(str1.find("&"))  # finds the first time the string & is occuring and returns its index . if not found then returns -1
# print(str1.isalnum())
# print(str1.isalpha())
# print(str1.islower())
# print(str1.isspace())
# print(str1.isprintable())
# print(str1.isspace())
# print(str1.istitle())
# print(str1.isupper())
# print(str1.startswith())
# print(str1.swapcase())
# print(str1.title())


#if else in python : 
# age=int(input("Your Age is : "))
# if(age>=18):
#      print("You can Vote ")
# else:
#     print("You cannot Vote ")
#     print("HMMMMMMMM")
#     print("NO") # inside the else statement 
# print("HELLO") #outside the else statement
# if else-if ladder  in python :  
# age=int(input("Enter Your Age : "))
# if(age <=0):
#     print("You Are a Kid")
# elif(age>=13 and age<18):
#     print("You are a teenager")
# elif(age>=19 and age<40):
#     print("You Are a Young Adult")
# else:
#     print("You are old ")
 #loops in python : 
 
 #for loop : 
 
# for i in range(1,20):
#     print(i)

# name="YASH"
# for i in name:
#     print(i)

# sports = ["Football ", "Cricket ", "Basketball","Badminton","VolleyBall","Kabaddi"]
# for game in sports :
#     print(game)
#     for i in range(9):
#         print(i)

# for i in range(1,100,2):
#     print(i)

#while loop :
# i=0
# while(i<=6):
#      print(i)
#      i+=1
     
# i=6
# while(i>=0):
#     print(i)
#     i-=1    

 # break and continue statements in python : 
 
# num= int(input("Enter the table number : "))
# for i in range(1,11):
#  if(i==5):
#      continue
#  print(num," X ",i," = ",num*i)
#  i+=1
# num= int(input("Enter the table number : "))
# for i in range(1,11):
#  if(i==5):
#      break
#  print(num," X ",i," = ",num*i)
#  i+=1

#infinite loop in python : 

# i=0
# while True:
#     if(i%2==0):
#         print(i)
#     i=i+1
#     if(i==100):
#         break

#functions in python : 
# def maxof(a,b):
#     if(a>b):
#         print("a is greater : ",a)
#     else:
#         print("b is greater : ",b)

# a=int(input("Enter your first  number : "))
# b=int(input("Enter your second number : "))   
# maxof(a,b)     
# def print_until_20():
#     for i in range(21):
#         print(i)
        
# print_until_20()
# def MYFUNC(a,b): # pass means that i can use the function later 
#      pass

#list in python : 

# marks=[0,30,2,4,5000,"Yash",True,7.55]
# for i in marks:
#  print(i)
# print(len(marks))
# print(marks[3])
# print(marks[-3])
# if "Yash" in marks:
#     print("Yash is present in the list ")
# print(marks[1:-3])
# print(marks[1:8:2]) #concept of jump index the third subscript means that it will jump that many places 
# list=[ i for i  in range(4)]
# print(list)
# list=[i for i in range(31) if i%2==0]
# print(list)

 #list methods in python : 
 
# l=[1,2,3,2,555,22,4,0]  
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# print(l.index(1))
# print(l.count(2))
# m = l.copy()
# m[2]=4
# print(l)
# l.insert(1,80)
# print(l)
# m=[200,300,500]
# l.extend(m)
# print(l)
# m=[0,1]
# k=l+m
# print(k)

#tuples in python : 
# tup= (1,2,3,4,5,6) # you cannot edit elements of a tuple , you cannot change value of tuple. it is immutable
# print(type(tup),tup)
# print(tup[0])
# print(tup[-2])
# print(len(tup))
# if 1 in tup:
#     print("Yes")
# else:
#     print("No")
# print(tup[-2 : 6])
# print(tup[0:4])
# tuple manipulations : to do manipulations to tuple. convert into list  then manipulate list and convert back into tuple

# tuple1=(1,2,3,4,5,"yash")
# tuple2=(1,2,3,4,5,6,"X")
# ans=tuple1+tuple2
# print(ans)
# print(type(ans))
# tuple1=(0,0,1,2,3,4,4,5,6,7,4,4,4,4,4,4)
# print(tuple1.count(4))
# print(tuple1.index(1))
# print(tuple1.index(2,3,5)) #()

#f strings in python 

# word="Hey my Name is {} and i Am from {}"
# Name="YASH"
# Country="India"
# print(f" Hey my Name is {Name} and i am From {Country}")
# price=50.89099
# print(f" FOR ONLY {price:.2f} DOllARS")
# print(f"{2*30}") 
# print(f" HEY my name is {{Name }} and i am from {{Country }}")
# print(type(f"{9*8}"))

#doc-strings in python :

# def square(n):
#     '''
#     gets square of a number  
#     '''
#     #the above is not comments 
#     return n**2
# n=int(input("Enter Number To Square : \n "))
# print(square.__doc__)
# result=square(n)
# print(result)

#     recursion in python :

# def factorial(n):
#      if(n==1 or n==0):
#          return 1
#      else:
#          return(n*factorial(n-1))
# number=int(input("Enter your number : "))
# answer=factorial(number)
# print("Here is Your Answer ", answer)

# def Fibonacchi(num):
#     if(num<2):
#         return num
#     else:
#         return(Fibonacchi(num-1)+Fibonacchi(num-2))
# n=int(input("Enter the Number of fibonacchi numbes you want to display : "))
# for i in range(n):
#     print(Fibonacchi(i))


# sets in python : 
 
 #sets are a data type which store unique elements. it is a collection of well defined objects , same like math, its unordered as well, set cannot be changed (element cannot be changed)
 
# set1={2,1,3,4,5}
# print(set1)
# set2={"yash",1,2,3,4,4,"yash"}
# print(set2)
# print(type(set2))
# set3=set() # to create a new empty set.
# #traversal in set
# for i in set2:
#     print(i)
#     #prints 1,2,3,4,yash
#set_methods in set:
# set1={1,2,3,4}
# set2={3,4,5}
# set3={1,2,3,4,5}
# print(set1.union(set2)) #union methods : gives union of sets without
# print(set1.update(set2))
# print(set1,set2) #updates the code by adding set 2 as well according to union
# print(set1.intersection(set2))# gives intersection of sets
# print(set1.update(set2))
# print(set1,set2)
#symmetric difference = (a U b)-(a N b ) N=intersection U=union. remove common values in both sets sets
# print(set1.symmetric_difference(set2))
# disjoint set : in a disjoint set, there are no common values in both sets
# print(set1.isdisjoint(set2))
# super-set: in a super-set , all the elements of the sub-set (set1) will be present in the (set 3)
# basically it means set3 is parent of child set1 and all elements of set1 will be present in set3.
# print(set3.issuperset(set1))
# set1.add(5) #adds a element in a set
# print(set1)
#you can add more than one element with the help of update
# set1.update(set2)
# print(set1)
#remove/discard
#removes an element present in a set.
# set1.remove(3)
# print(set1)
# discard removes an element but it doesnt show error if element is not present 
# set1.discard(56)
# print(set1)
# set1.pop()
# print(set1) #pops a random element from a set 
#you can delete an entire set with the help of del keyword
# del set1 #deletes set1
# print(set2) 

#dictionaries in python : 
#dictionaries are key value pairs of collection of data , they can store multiple items in a single variable
# dic ={key : value , key1: value1 .....}
# name = {
#     1:"YASH",
#     2:"PERSON_2",
#     3:"PERSON_3"
# }
# print(name)

#accessing in dictionary 
# print(name[3]) #can access by mentioning key
# print(name.get(3)) #can access by get keyword as well
# print(name.get('AAYEIN')) #gives NONE if the value is not present in dictionary
# print(name.keys()) #gets keys in dictionary
# for key in name.keys(): #gets all keys in python
#     print(name[key])
# print(name.values()) #gets values in dictionary
#we can also use f strings and access keys in this way as well
# for key in name.keys():
#     print(f"the value corresponding to the key {key} is : {name[key]}")
# item keyword gets us key value pairs in the dictionary
# for key,value in name.items():
#     print(f"the value corresponding to the key {key} is:{value}")

#dictionary methods : 

# name={
#     1:"INDIA",
#     2:"PAKISTAN",
#     3:"NEPAL",
#     4:"SRILANKA",
#     5:"BANGLADESH",
#     6:"MYANMAR ",
#     7:"CHINA",
#     8:"BURMA"
# }
# name.update({2:"NORTH KOREA"}) #updates the value of the dictionary with another value 
# print(name)

# name.clear() #clears the dictionary and an empty dictionary is printed 
# print(name)
 
# name.pop(5)
# print(name) # pops or removes the value corresponding to the key  mentioned

# name.popitem() #pops out last key value pair in dictionary
# print(name)

# del name[5] #deletes the value corresponding to the value mentioned
# print(name)

#loops with else in python :

# for i in range(5):
#     print(i)
# else:
#     print("EXECUTED AFTER ALL THE ITERATIONS ARE FINISHED , loop did not break but loop is finished")

# i=0
# while i<5:
#     print(i)
#     i+=1
# else:
#     print("EXECUTED AFTER ALL ITERATIONS ARE FINISHED , loop finsihes but does not break")

#exception handling in python : used to handle errors , it is used to avoid a program from crashing ,without this process ,exceptions would disrupt the normal operations of the program
#using try except to handle errors in python 
# a=input("enter a number ")
# print(f"Multiplication table of {a} is :  ")
# try:
#  for i in range (1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print("SORRY SOME ERROR OCCURED ")
# print("SOMEthing")

# try:
#     num=int(input("ENTER AN INETEGR INPUT : "))
#     print(num)
# except ValueError:
#     print("THE VALUE YOU ENTERED IS INVALID ")

# try:
#     num1=int(input("ENTER A NUMBER : \n"))
#     num2=int(input("ENTER A NUMBER : \n"))
#     division=num1/num2
#     print(division)
# except ZeroDivisionError:
#     print("YOU CANNOT DIVIDE A NUMBER BY 0")
# except ValueError:
#     print("SORRY THE VALUE YOU ENTERED IS INVALID ")
#finally keyword in error handling  : basically used in functions 
# def Myfunc():
#     try:
#         num1=int(input("Enter any number "))
#         print(num1)
#         return 1
#     except:
#      print("Some Error Occured ")
#      return 0
     
#     finally:
#         print("I AM ALWAYS EXECUTED ")
    
# x=Myfunc()
# print(x)
#raising custom errors in python : 

# a=int(input("Enter any number between 1 and 10 : \n"))
# if(a<1 or a>100):
#     raise ValueError("INVALID INPUT ! , PLEASE TRY AGAIN ")



# a = input("Enter any value between 5 and 9 : ")
# if a == "quit":
#     print("you choosed to quit")
# elif (int(a) < 5 or int(a) > 9):
#     raise ValueError("Value should be between 5 and 9")


#short-hand if else statements in python : improves readability if there are less if-else statements < 1 . 
# a=9000
# b=700
# c= True if(a>b) else False
# print(c)

#enumarate statements in python : used to loop over a sequence and you can get its index and value 
# marks=[100,20,1,4,5,6,7,990]
# for index,marks in enumerate(marks):
#  print(f"{index+1}:{marks}")
#  if(index==7):
#   print("Good Job")
#   break
#the index starts with 0 by default while using enumarate 
#import in python :

# import math
# print(math.ceil(999.090))
# print(math.floor(999.090))
# from math import sqrt,pi
# result=sqrt(9)*pi
# print(result)
# def welcome():
#     print("HI")

# if __name__="__main__" in python : 
    
#The expression __name__ == "__main__" is commonly used to determine whether the Python script is being run directly or if it's being imported as a module into another script.
# welcome() as you can see that welcome runs 2 times due to importing , in yash.py . 
# def welcome():
#     print("HI")
#     #this is run directly in the script so it is set to  __main__
#     print(__name__)
# if __name__=="__main__":
#   welcome()
# When the script is executed directly (i.e., it's the entry point of the program), Python sets __name__ to "__main__".
# When the script is imported as a module into another script, Python sets __name__ to the name of the module.


#os module in python : helps to interact with operating system 
# import os
# if( not os.path.exists("data")):
#    os.mkdir("data")
# for i in range(0,100):
#     os.rename(f"Data/Day{i+1}",f" Data/Day:{i+1}")










    

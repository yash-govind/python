#Secret Code Language in Python : 
import random
import string
s="" #empty string 

def code():
    global s
    if(len(s)>=3):
        s=s[1:]+s[0] #remove the first index and append the last index to string.
        random_characters = ''.join(random.choices(string.ascii_letters + string.digits,k=3)) #random characters 
        modified_string=random_characters+s+random_characters #concatenate random characters at the end and at the beginning of string
        return modified_string #return the modified string
    else:
        return(s[::-1]) #[start:stop:step] start is at the beginning , end is at the end and step is -1 so its reverse.it prints reverse for every 1st step
    #print the reversed string 
def decode():
    global s
    if(len(s)<3):
        return(s[::-1]) #reverse the string if the string has less than 3 characters
    else:
        s=s[3:-3] #remove 3 letters at start and 3 letters at the end 
        modified_string=s[:-1]+s[0] #remove the last letter and then append it to the beginning 
        return modified_string #print the modified string
    
user_input=int(input("DO YOU WANT TO CODE OR DECODE  , PRESS 1 for Code and 2  for Decode"))-1
if(user_input==1):
    modified_s=code()
    print(modified_s)
elif(user_input==2):
    modified_s=decode()
    print(modified_s)
else:
    print("INVALID INPUT ")
    
    





        
        

        
        
        
        
        
    
 
         
         
     
         
 
    
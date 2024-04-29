import time
watch=time.strftime("%H:%M:%S") #get time in hr min secs 
print( "This is the Current Time :",watch)
watch=int(time.strftime("%H"))
if (12<=watch<17) :
    print(" GOOD AFTERNOON SAR/MEDAM") #12-16 hrs is afternnoon
elif (17<=watch<=19):
    print("GOOD EVENING SAR/MEDAM") #17-19 hrs is evening 
elif (20<=watch<24 or 0<=watch<5): # 20-23hrs is night but 0 to 4 hrs is also night 
    print("GOOD NIGHT SAR/MEDAM")
else:
    print("GOOD MORNING SAR/MEDAM") # 5-11 is morning 
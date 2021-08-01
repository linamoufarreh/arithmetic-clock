current_time= input("Enter current time: ")
duration = input("Enter the duration: ")

hours= int(current_time[0:2])
minutes= int(current_time[3:5])
seconds= int(current_time[6:8])

if len(duration)==6:
    minutes= minutes+ int(duration[3:5])
    hours= hours+ int(duration[0:2])
else:
    minutes= minutes+ int(duration[0:2])
    hours= 0 + hours
    
if "PM" in current_time:
    hours= hours +12
    if hours>=24:
        hours= 24-hours
        
if minutes>=60:
    hours= hours +1
    minutes= minutes-60
else:
    minutes= 0 + minutes
    
print(hours, end=" hours ")
print(minutes, end=" minutes ")
print(seconds, end=" seconds ")

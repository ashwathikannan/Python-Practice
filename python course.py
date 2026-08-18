day=int(input("enter the day:"))
month=int(input("enter the month:"))
year=int(input("enter the year:"))

if (year%4==0 and year%400==0) or year%100!=0 :
    leap= True
else:
    leap= False
    
if month ==2:
    max_days=29 if leap else 28
elif month in [4,6,9,11]:
    max_days=30
elif month in [1,3,5,7,8,10,12]:
    max_days=31
else:
    max_days=0

if max_days!=0 and 1<=day<=max_days:
    print("valid date")
else:
    print("invalid date")

age1=int(input("enter the age of person 1:"))
age2=int(input("enter the age of person 2:"))
age3=int(input("enter the age of person 3:"))
if age1<age2 and age1<age3:
    print("person 1 is youngest!")
elif age2<age1 and age2<age3:
    print("person 2 is youngest!")
else:
    print("person 3 is the youngest!")

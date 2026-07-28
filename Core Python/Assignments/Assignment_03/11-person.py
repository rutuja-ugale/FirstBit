age1 = int(input("enter the age for 1 person::"))
ticket1 = 100
#  1 person
if(age1 < 12):
    amt1 = ticket1 - (ticket1*12/100)
    print("for 1 person::",amt1)
elif(age1 > 59):
    amt1 = ticket1 - (ticket1*50/100)
    print("for 1 person::",amt1)
else:
    amt1 = ticket1
    print("for 1 person::",amt1)
#  2 person
age2 = int(input("enter the age for 2 person::"))
ticket2 = 100
if(age2 < 12):
    amt2 = ticket2 - (ticket2*12/100)
    print("for 2 person::",amt2)
elif(age1 > 59):
    amt2 = ticket2 - (ticket2*50/100)
    print("for 2 person::",amt2)
else:
    amt2 = ticket2
    print("for 2 person::",amt2)
#  3 person
age3 = int(input("enter the age for 3 person::"))
ticket3 = 100
if(age1 < 12):
    amt3 = ticket3 - (ticket3*12/100)
    print("for 3 person::",amt3)
elif(age1 > 59):
    amt3 = ticket3 - (ticket3*50/100)
    print("for 3 person::",amt3)
else:
    amt3 = ticket3
    print("for 3 person::",amt3)
#  4 person
age4 = int(input("enter the age for 4 person::"))
ticket4 = 100
if(age1 < 12):
    amt4 = ticket4 - (ticket4*12/100)
    print("for 4 person::",amt4)
elif(age1 > 59):
    amt4 = ticket4 - (ticket4*50/100)
    print("for 4 person::",amt4)
else:
    amt4 = ticket4
    print("for 4 person::",amt4)
#  5 person
age5 = int(input("enter the age for 5 person::"))
ticket5 = 100
if(age1 < 12):
    amt5 = ticket5 - (ticket5*12/100)
    print("for 5 person::",amt5)
elif(age1 > 59):
    amt5 = ticket5 - (ticket5*50/100)
    print("for 5 person::",amt5)
else:
    amt5 = ticket5
    print("for 5 person::",amt5)
tot_amt = amt1 + amt2 + amt3 + amt4 + amt5
print("total amount is:",tot_amt)
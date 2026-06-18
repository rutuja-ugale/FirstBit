cp = int(input('Enter Cost Price: '))
sp = int(input('Enter Selling Price: '))
# amt = sp - cp 
# if(amt > 0)
if(sp > cp):
    print('Profit is: ', sp - cp)
elif(sp == cp):
    print('No profit no Loss')
else:
    print('Loss is: ', cp - sp)
username = "rutuja"
userpass  = "1234"

userid = input("Enter username: ")
userpwd = input("Enter Password: ")

if(username == userid and userpass == userpwd):
    print("login successful")
else:
    print("Invalid Credentials Try Again")
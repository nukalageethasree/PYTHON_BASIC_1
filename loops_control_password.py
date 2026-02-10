correct_password="python123"
attempts=3
while attempts>0:
    password=input("enter the password:")
    if password==correct_password:
        print("the given password is correct")
        break
    else:
        attempts-=1
        print("wrong password and attempt left:",attempts)
if attempts==0:
    print("locked")        
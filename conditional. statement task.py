
# practice conditional statement
#simple  if statement
x=5
if x>10:
    print("x is greater than 10")
else:
    print("x is less than equal to 10")


# if -elif-else statement
x=5
if x>10:
  print("x is greater than 10")
elif x==5:
    print("x is equal  to 5")
    print("x is less than to 5")

#nested if statement
x=5
y=10
if x > 5:
    if y >10:
        print("x is greater than 5 and y is greater than 10")
    else:
        print("x is greater than 5 and y is less than  or equal  to 10")
else:
   print("x is less than or equal to 5")

# complete the conditional statements task using input functions
# simply if statementwith user input

x=float (input("Enter aa number:"))
if x>10:
    print("the number is greater than 10")
else:
    print("the number is less than or equal to 10")



    #if -elif- else statement with  user input
    age =int(input("enter  your age:"))
    if age>=18:
        print(" you are eligible to vote:")
    elif age>=13:
        print("you are a teenager")
    else:
        print("you are a kid")


#nested if statement with user input

username=input("Enter your username:")
password=input("Enter your password: ")
if username=="admin":
    if password=="password 1234":
        print("login  successful")
    else:
        print("incorrect password")
else:
  print("incorrect username")




# for loop---> to iterate over a sequence 
# syntax
# for variable in sequence
#  # statement 1
#  #statement 2

list_1=["ravi" , "krishna", "koushik", "arjuna", "ram"]
for i in  list_1:
    print(i)

fruits=['apple', 'cheery', 'orange', 'papaya']
for fruit in fruits:
    print(f"{fruit} stock received")

employee_data= ["ravi", "jyothi", "satya", "venu", "priya"]
for i in employee_data:
    print(f"{i} salary 10 % hike given")


#range(stop)
#range(start,stop)
#range(start, stop, step)
for i in range(10):
    print(i)

for i in range(2,11):
    print(i)

for i in range(1,11,2,):
    print(i)
for i in range(499,1001):
    print(i)


#multiplication of 2 table
for i in range(1,11):
    print(f"2x{i}={i*2}")
for i in range(1,21):
    print(f"17x{i}={i*17}")

#syntax
#nested for loop
# for i in sequence:
for i in range(5):#outer loop
    for j in range(5): #inner loop
        print(i,j)
        # multiplication table
    for i in range(1,11):
        for j in range(1,21):
            print(f"{i}x{j}={i*j}")
            print()
        # update price
        prices=(99,100,200,101)
        for i in prices:
            print(i+2)
        #syntax
        #while condition:true
        # # block of code

        age =18
        while age >=18:# true
            print("you are eligible to vote")
            break
        count=0
        while count<3:
            print(count)
            count+=1

        while True:
            user_name =input("enter username:")
            password=input("enter the password:")
            if user_name=="ravi" and password=="1456":
                print("login success")
                break
            else:
                print("invalid credentials")
            #while condition:
            #    while condition:
            age = 60
            while age>=45: #outer while loop
                print("this is outer while loop")
                age-=1
                print(age)
                while age >=45:# inner while loop
                    print("this is inner while loop")
                    break
                for i in range(0,10,1):
                    print(i)

                outer=0
                while outer<3:
                    inner=0
                    while inner<2:
                        print(outer,inner)
                        inner+=1
                    outer+=1
                    while True:
                        print("hello")













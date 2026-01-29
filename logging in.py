attempts = 0
max_attempts = 3
while attempts < max_attempts:
    password = input("enter your password: ")
    if password =="admin123":
     print("log in successfull")
    break
attempts +=1

#payments
payments = [3000,2500,800]
total = 0
for amount in payments:
   total +=amount
   print("total collected amount:", total)


   
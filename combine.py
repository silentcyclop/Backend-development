#combing input and function 
def check_age(age):
    return 'ADULT'if age>=18 else "minor"
age = int(input("please enter your age"))
print(check_age(age))
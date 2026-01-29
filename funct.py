#grade
def average_grade(grades):
    total = sum(grades)
    return total / len(grades)
grades = [80, 90, 75]
avg = average_grade(grades)
print("Average:", avg)
 

#example
age = float(input("enter your age"))
if age>18:
    print("your an adult")
else:
    print("you are a minor")
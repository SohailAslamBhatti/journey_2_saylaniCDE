```python
#  Part -1 Python Basics (Variables)
## 1. Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
```


```python
print("Name:\t\tSohail Aslam Bhatti")  
print("Father's Name:\tMuhammad Aslam Bhatti") 
print("Date of Birth:\t17-05-1992\n")
print("Name: Sohail Bhatti\nFather's Name: Muhammad Aslam Bhatti\nDate of Birth: 17-05-1992")
```

    Name:		Sohail Aslam Bhatti
    Father's Name:	Muhammad Aslam Bhatti
    Date of Birth:	17-05-1992
    
    Name: Sohail Bhatti
    Father's Name: Muhammad Aslam Bhatti
    Date of Birth: 17-05-1992
    


```python
## 2. Write your small bio using variables and print it using print function"
```


```python
name = "Sohail Aslam Bhatti"
father_name = "Muhammad Aslam Bhatti"
dob = "17-05-1992"
hobby = "Coding/ Cruising"
city = "Karachi, Pakistan"

# Printing the bio
print("My Name:\t", name)
print("Father's Name:\t", father_name)
print("Date of Birth:\t", dob)
print("Hobby:\t\t", hobby)
print("City:\t\t", city)
```

    My Name:	 Sohail Aslam Bhatti
    Father's Name:	 Muhammad Aslam Bhatti
    Date of Birth:	 17-05-1992
    Hobby:		 Coding/ Cruising
    City:		 Karachi, Pakistan
    


```python
## 3. Write a program in which use all the operators we can use in Python
```


```python
# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)   
print("a - b =", a - b)   
print("a * b =", a * b)   
print("a / b =", a / b) 
print("a % b =", a % b)  
print("a ** b =", a ** b) 
print("a // b =", a // b)
print()

# 2. Assignment Operators
x = 5
print("Assignment Operators:")
x += 2 
print("x += 2 →", x)
x -= 1
print("x -= 1 →", x)
x *= 3
print("x *= 3 →", x)
x /= 2
print("x /= 2 →", x)
x %= 4
print("x %= 4 →", x)
x **= 2
print("x **= 2 →", x)
x //= 3
print("x //= 3 →", x)
print()

# 3. Comparison (Relational) Operators
print("Comparison Operators:")
print("a == b:", a == b) 
print("a != b:", a != b)  
print("a > b:", a > b)   
print("a < b:", a < b)   
print("a >= b:", a >= b) 
print("a <= b:", a <= b) 
print()

# 4. Logical Operators
p = True
q = False
print("Logical Operators:")
print("p and q:", p and q)  
print("p or q:", p or q)    
print("not p:", not p)      
print()

# 5. Membership Operators
name = "Sohail"
print("Membership Operators:")
print("'S' in name:", 'S' in name)     
print("'x' not in name:", 'x' not in name)  
print()

# 6. Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("Identity Operators:")
print("x is z:", x is z)        
print("x is y:", x is y)      
print("x is not y:", x is not y)
```

    Arithmetic Operators:
    a + b = 13
    a - b = 7
    a * b = 30
    a / b = 3.3333333333333335
    a % b = 1
    a ** b = 1000
    a // b = 3
    
    Assignment Operators:
    x += 2 → 7
    x -= 1 → 6
    x *= 3 → 18
    x /= 2 → 9.0
    x %= 4 → 1.0
    x **= 2 → 1.0
    x //= 3 → 0.0
    
    Comparison Operators:
    a == b: False
    a != b: True
    a > b: True
    a < b: False
    a >= b: True
    a <= b: False
    
    Logical Operators:
    p and q: False
    p or q: True
    not p: False
    
    Membership Operators:
    'S' in name: True
    'x' not in name: True
    
    Identity Operators:
    x is z: True
    x is y: False
    x is not y: True
    


```python
## 4. Completes the following steps of small task:\n",
##      - Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables\n",
##      - Mention Variable of Total Marks and assign 300 to it\n",
##      - Calculate Percentage
```


```python
english = 85
islamiat = 90
maths = 95

total_marks = 300

obtained_marks = english + islamiat + maths

percentage = (obtained_marks / total_marks) * 100

print("Marks in English:", english)
print("Marks in Islamiat:", islamiat)
print("Marks in Maths:", maths)
print("\nTotal Marks:", total_marks)
print("\nObtained Marks:", obtained_marks)
print("\nPercentage:", percentage, "%")
```

    Marks in English: 85
    Marks in Islamiat: 90
    Marks in Maths: 95
    
    Total Marks: 300
    
    Obtained Marks: 270
    
    Percentage: 90.0 %
    


```python
#  Part - 2: Python Basics (Conditional Statements)
## 1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.\n",
##    "Ask user for their salary and year of service and print the net bonus amount.
```


```python
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    bonus = salary * 0.05
    print("Congratulations! You are eligible for a bonus of:", bonus)
else:
    bonus = 0
    print("Sorry, no bonus as your service is less than or equal to 5 years.")

print("Net Bonus Amount =", bonus)
```

    Enter your salary:  50000
    Enter your years of service:  6
    

    Congratulations! You are eligible for a bonus of: 2500.0
    Net Bonus Amount = 2500.0
    


```python
## 2) Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
```


```python
age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")
```

    Enter your age:  35
    

    You are eligible for voting.
    


```python
## 3) Write a program to check whether a number entered by user is even or odd.
```


```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")
```

    Enter a number:  122
    

    122 is an Even number.
    


```python
## 4) Write a program to check whether a number is divisible by 7 or not.\n", "Show Answer"
```


```python
num = int(input("Enter a number: "))

if num % 7 == 0:
    print(num, "is divisible by 7.")
else:
    print(num, "is not divisible by 7.")
```

    Enter a number:  147
    

    147 is divisible by 7.
    


```python
## 5) Write a program to display \n",
##    "\"Hello\" if a number entered by user is a multiple of five , otherwise print \"Bye\"."
```


```python
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("\nHello")
else:
    print("\nBye")
```

    Enter a number:  125
    

    
    Hello
    


```python
## 7) Write a program to display the last digit of a number.\n
```


```python
num = int(input("Enter a number: "))

last_digit = num % 10

print("The last digit of", num, "is:", last_digit)
```

    Enter a number:  157
    

    The last digit of 157 is: 7
    


```python
## 9) Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
```


```python
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

if length == breadth:
    print("It is a Square.")
else:
    print("It is a Rectangle.")
```

    Enter the length:  6
    Enter the breadth:  8
    

    It is a Rectangle.
    


```python
## 10) Take two int values from user and print greatest among them.
```


```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater.")
elif num2 > num1:
    print(num2, "is greater.")
else:
    print("Both numbers are equal.")
```

    Enter first number:  5
    Enter second number:  7
    

    7 is greater.
    


```python
## 11) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.\n",
##    "Ask user for quantity\n",
##    "Suppose, one unit will cost 100.\n",
##    "Judge and print total cost for user."
```


```python
quantity = int(input("Enter the quantity: "))

unit_price = 100

total_cost = quantity * unit_price

if total_cost > 1000:
    discount = total_cost * 0.10
    total_cost = total_cost - discount
    print("You got a 10% discount of:", discount)

print("Total cost to pay:", total_cost)
```

    Enter the quantity:  25
    

    You got a 10% discount of: 250.0
    Total cost to pay: 2250.0
    


```python
## 12) A school has following rules for grading system: ",
##  a. Below 25 - F,
##  b. 25 to 45 - E,
##  c. 45 to 50 - D,
##  d. 50 to 60 - C,
##  e. 60 to 80 - B,
##  f. Above 80 - A,
##  Ask user to enter marks and print the corresponding grade.
```


```python
marks = int(input("Enter your marks: "))

if marks < 25:
    grade = "F"
elif marks <= 45:
    grade = "E"
elif marks <= 50:
    grade = "D"
elif marks <= 60:
    grade = "C"
elif marks <= 80:
    grade = "B"
else:
    grade = "A"

print("Your Grade is:", grade)
```

    Enter your marks:  75
    

    Your Grade is: B
    


```python
## 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.", 
##    Take following input from user, 
##    - Number of classes held, 
##    - Number of classes attended, 
##    - And print percentage of class attended, 
##    - Is student is allowed to sit in exam or not.
```


```python
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance = (classes_attended / classes_held) * 100

print("Attendance Percentage:", attendance, "%")


if attendance >= 75:
    print("You are allowed to sit in the exam.")
else:
    print("You are NOT allowed to sit in the exam.")
```

    Enter number of classes held:  75
    Enter number of classes attended:  67
    

    Attendance Percentage: 89.33333333333333 %
    You are allowed to sit in the exam.
    


```python
## 15) Modify the above question to allow student to sit if he/she has medical cause. 
##     Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
```


```python
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance = (classes_attended / classes_held) * 100

print("Attendance Percentage:", attendance, "%")

medical = input("Do you have a medical cause? (Y/N): ")

if attendance >= 75:
    print("You are allowed to sit in the exam.")
elif medical.upper() == "Y":
    print("You are allowed to sit in the exam due to medical cause.")
else:
    print("You are NOT allowed to sit in the exam.")
```

    Enter number of classes held:  75
    Enter number of classes attended:  67
    

    Attendance Percentage: 89.33333333333333 %
    

    Do you have a medical cause? (Y/N):  y
    

    You are allowed to sit in the exam.
    


```python
## 16) Write a program to check if a year is leap year or not, 
##     "If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
```


```python
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year ")
else:
    print(year, "is NOT a Leap Year ")
```

    Enter a year:  2020
    

    2020 is a Leap Year 
    


```python
## 17) Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service., 
##     - if employee is female, then she will work only in urban areas, 
##     - if employee is a male and age is in between 20 to 40 then he may work in anywhere, 
##     - if employee is male and age is in between 40 t0 60 then he will work in urban areas only, 
##       And any other input of age should print \"ERROR\"
```


```python
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
marital_status = input("Are you married? (Y/N): ").upper()

if gender == "F":
    print("You will work only in Urban areas.")
elif gender == "M":
    if 20 <= age <= 40:
        print("You may work anywhere (Urban or Rural).")
    elif 40 < age <= 60:
        print("You will work only in Urban areas.")
    else:
        print("ERROR: Invalid age for service.")
else:
    print("ERROR: Invalid gender input.")
```

    Enter your age:  37
    Enter your gender (M/F):  m
    Are you married? (Y/N):  y
    

    You may work anywhere (Urban or Rural).
    


```python
## 6) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 
#     Unit Price, 
#     uptp 100 units no charge, 
#     Next 200 units Rs 5 per unit, 
#     After 200 units Rs 10 per unit, 
#     For example if input unit is 350 than total bill amount is Rs.3500, 
#     For example if input unit is 97 than total bill amount is Rs.0, 
#     For example if input unit is 150 than total bill amount is Rs.750"
```


```python
units = int(input("Enter number of units consumed: "))

bill = 0

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + ((units - 300) * 10)

print("Total Electricity Bill = Rs.", bill)
```

    Enter number of units consumed:  200
    

    Total Electricity Bill = Rs. 500
    


```python
## 13) Take input of age of 3 people by user and determine oldest and youngest among them.
```


```python
age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))

oldest = max(age1, age2, age3)

youngest = min(age1, age2, age3)

print("Oldest age is:", oldest)
print("Youngest age is:", youngest)
```

    Enter age of first person:  24
    Enter age of second person:  34
    Enter age of third person:  17
    

    Oldest age is: 34
    Youngest age is: 17
    


```python

```

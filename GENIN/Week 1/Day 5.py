#Day 5 - Loops, Range and Code Block

# Average Height Exercise
student_heights = input("Input the list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0 
for height in student_heights:
    total_height += height
print(total_height)

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(num_of_students)

average_height = round(total_height / num_of_students)
print(average_height)

# - Password Generator
import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', ' 3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
n_alphabets = int(input("Your password would contain how many letters? \n"))
n_numbers = int(input("You would like how many numbers? \n"))
n_symbols = int(input("Symbols? \n"))


password = ""
for char in range(1, n_alphabets + 1):
    password += random.choice(alphabets)

for char in range(1, n_numbers + 1):
    password += random.choice(numbers)

for char in range(1, n_symbols + 1):
    password += random.choice(symbols)
print(password)


password_list = []
for char in range(1, n_alphabets + 1):
    password_list.append(random.choice(alphabets))

for char in range(1, n_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, n_symbols + 1):
    password_list += random.choice(symbols)
   
print(password_list)
random.shuffle(password_list)
print(str(password_list))

password = ""
for char in password_list:
    password += char
print(password) 
#Complete
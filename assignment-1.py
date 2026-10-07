# Section 1: Variables and Types

name = "Betty"
age = 26
height = 5.8
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2: User input and Math

name = input("What is your name? ")
birth_year = input("What year were you born? ")
current_year = 2026
approx_age = (current_year - int(birth_year))

print("Hi " + name + ", you are approximately " + str(approx_age) + " years old.")

# Section 3: Type Conversion and f-strings

first_number = float(input("Enter a number: "))
second_number = float(input("Enter another number: "))
product_of_numbers = (first_number * second_number)

print(f"{first_number} x {second_number} = {product_of_numbers}")

# Section 4: Formatted Recipt

item_name = "Graphic Novel Series"
price = 9.99
quanity = 9
total = (price * quanity)

print("========================")
print("     RECEIPT     ")
print("========================")
print(f"Item:    {item_name}")
print(f"Price:   ${price}")
print(f"Quanity: {quanity}")
print("------------------------")
print(f"Total:   ${total:.2f}")
print("========================")

# Section 5: Mini Project - Profile Card

user_name = input("What is your name? ")
user_hometown = input("Where do you call your hometown? ")
user_hobby = input("What is your favorite hobby? ")
user_fun_fact = input("What is a fun fact about you? ")
user_birth_year = int(input("What year were you born? "))
current_year = 2026
user_age = (current_year - user_birth_year)


print("==============================")
print(f"     PROFILE: {user_name}    ")
print("==============================")
print(f"Hometown:  {user_hometown}")
print(f"Hobby:     {user_hobby}")
print(f"Fun Fact:  {user_fun_fact}")
print(f"Age:       {user_age}")

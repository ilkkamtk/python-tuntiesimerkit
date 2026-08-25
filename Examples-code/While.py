# enter even number: 
number = int(input("Please enter a positive integer: "))

if number <= 0:
    print("Error: please enter a positive integer.")
else:
    
    # current_num = 0
    # while current_num <= number:
    #     print(current_num)
    #     current_num = current_num + 2

    current_num = 0
    while current_num <= number:
        if current_num % 2 == 0:
            print(current_num)
        current_num = current_num + 1 # current_num += 1

# Sum until 1000:
total = 0
iteration = 0

while total <= 1000:
    number = int(input("Enter an integer: "))
    total = total + number
    iteration = iteration + 1

print("The final sum is", total)
print("The numbers of times were asked from user:", iteration, "times")

# falling object: 
gravity = 9.81

initial_height = float(input("Enter the initial height in metres: "))

time = 0
current_height = initial_height

while current_height > 0:
    time = time + 1
    fallen_distance = 0.5 * gravity * time ** 2
    current_height = initial_height - fallen_distance
    if current_height < 0:
        current_height = 0
    print(f"At {time} seconds, Height {current_height:.2f} m")

print(f"The object took {time} seconds to reach the ground.")

# Multiplication table: 
first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second}")
        second = second + 1
    first = first + 1

# Fractorial number: 
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break

    factorial = 1
    new = 1
    while new <= number:
        factorial *= new
        new += 1
    print(f"The factorial of the number {number} is {factorial}")
print("Thanks and bye!")

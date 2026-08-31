# --------print all characters ------------
name = input("Enter your name: ")
for character in name: 
    print(character)

#-------- input positive number ------------
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Error: please enter a positive integer.")
else:
    # use steps to print even num
    for i in range(0, number + 1, 2): 
        print(i)
    # use if to check even num
    for i in range(number + 1):
        if i % 2 == 0:
            print(i)

# ---------- number list -----------
numbers = []

while True:
    entry_num = input("Enter a number: ")
    if entry_num == "":
        break
    numbers.append(int(entry_num))

printed_list = []

for number in numbers:
    if number > 100 and number not in printed_list:
        print(number)
        printed_list.append(number)

#------- print 1st letter ------
sentence = input("Enter a sentence: ")
sentence = " " + sentence
for index_num in range(1, len(sentence)):
    if sentence[index_num -1] == " " and sentence [index_num] != " ": 
        print(sentence[index_num])
    index_num += 1
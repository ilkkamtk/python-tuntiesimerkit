# python lesson examples

[suomi](README.md) | [english](README_en.md)

## Module 3 - Variables, etc.

Write a Python program that asks the user for two numbers: the radius of a circle and the side length of a square. The program should calculate the areas of both shapes and store them in variables. Finally, the program should print both areas.

---

Write a program that asks the user for the amount of three different fruits in kilograms.  
The program calculates the price using the following fixed prices per kilogram:

* Banana: €2.85/kg
* Apple: €3.15/kg
* Orange: €4.05/kg

The program should calculate and display the price of each fruit separately, as well as the total price of all fruits.

**Example of the program's operation**

```monospace
Enter the amount of bananas (kg).
1.2

Enter the amount of apples (kg).
2.5

Enter the amount of oranges (kg).
0.8

Shopping summary:
Bananas: €3.42
Apples: €7.88
Oranges: €3.24
Total: €14.54
````

---

Write a program that functions as a simple dice simulator. The program should randomly roll and print the results of two dice. One die is six-sided (numbers 1–6) and the other is twenty-sided (numbers 1–20). Finally, the program should calculate and print the total sum of both dice.

---

## Module 4 - Conditional statement (if)

Write a program that asks the user for their age. The program should check the age and tell the person whether they are old enough to vote in Finnish parliamentary elections. If the person is not of legal age, the program should state how many years they still have until they reach legal age and the right to vote. In Finland, the voting age is 18 years.

---

Write a program that asks the user for their electricity consumption in kilowatt-hours (kWh). The program should calculate the electricity bill based on three different tiered prices and print the final amount.

* **The first 50 kWh** cost €0.10/kWh.
* **The next 150 kWh** cost €0.08/kWh.
* **Consumption over 200 kWh** costs €0.06/kWh.

---

Write a program that asks the user for their performance in three different subjects: physics, mathematics, and chemistry. The program should tell the user if they received a scholarship.

A scholarship is granted if:

the user's result is over 90 in both physics and mathematics
or

the user's result is over 95 in chemistry.

In addition, the program must indicate if the result in any subject is below 50. In this case, the user cannot receive a scholarship, even if the other conditions are met.

---
Write a program that takes a letter of the alphabet as input.
If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel.
If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant.
Otherwise your program should display a message indicating that the letter is a consonant.

---

## Module 5 - Pre-conditioned loop (while)

Write a program that asks the user for a positive integer. The program should calculate and print all even numbers from 0 up to the number given by the user. If the user enters a negative number or zero, the program should print an error message.

---

Write a program that asks the user for integers one at a time. The program calculates the sum of the numbers and asks for a new number until the sum exceeds 1000. After this, the program prints the final sum and states how many numbers were asked from the user.

---

Write a program that simulates a falling object.

The program asks the user for the initial height of the object in meters. After this, it calculates and prints the object's height second by second using a **while** loop. The loop continues until the object's height is zero or less. Finally, the program prints the total time it took for the object to fall.

The distance of a falling object (\$s\$) as a function of time (\$t\$) is calculated with the formula:
\$s = \frac{1}{2}gt^2\$, where the acceleration due to gravity (\$g\$) is approximately \$9.81 m/s^2\$.

Therefore, in each loop iteration, the program should calculate the current height of the object by substracting the fallen distance from the initial height.

---
Write a programme that print out the multiplication table from 1 to 5 using nested loop.

---
Write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.The program should use **while true** and **break**. 

---

## Module 6 - List structure and exhaustive loop (for)

---
Write a program that asks user to input a name, then prints out all characters of the name using for loop.
---
Write a program that asks the user for an integer. The program should calculate and print all even numbers from 0 up to the number given by the user using a **for** loop. If the user enters a negative number or zero, the program should print an error message.

---

Write a program that asks the user for numbers until they enter an empty string as a termination character. The numbers are stored in a list. After this, the program should iterate through the list's elements and print the unique numbers that are greater than 100. Print each number only once, even if it was entered more than once.

---
Write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

---

## Module 7 - Function

Write a function that takes two integers as parameters and returns their sum. Call the function in the main program and print the value it returns.

---

Write a function that takes a list of strings as a parameter (e.g., names or words). The function returns a new list containing only the strings from the original list that have a length of more than five characters.

Write a main program where:

1. You create a sample list of strings (e.g., animal names: `"cat"`, `"dog"`, `"elephant"`, `"lion"`, `"giraffe"`).
2. You call the function you created with this list.
3. You print both the original list and the filtered list returned by the function.

---

## Module 8 - Tuple, set and dictionary

Write a program that asks the user for three different fruits and their amounts in kilograms. Store the fruits and their amounts in a dictionary where the fruit's name is the key and the amount is the value. The program should print the dictionary.

---

Write a program that asks the user for numbers one at a time. The program continues to ask for numbers until the user enters 0. The numbers are stored in a list. After this, the program should print the list without duplicates, meaning only the unique numbers that were entered.

**Hint:**
You can create a new set from the list, which automatically removes all duplicates. You can then convert the set back into a list if you need list functionalities.

---

Write a program that functions as a simple phonebook. The program asks the user whether they want to add a new contact, search for an existing contact, or quit.

If the user chooses to add a new contact, the program asks for the contact's name and phone number.

If the user chooses to search, the program asks for a name and prints the corresponding phone number.

If the user wants to quit, the program terminates.

The program should store the data in a dictionary and allow the user to select actions multiple times until they decide to quit. The program must also handle the situation where the user tries to search for a name that does not exist.

The program can be extended by using a nested data structure. Now the phonebook is a LIST, and each contact is a DICTIONARY with keys: name, id, date_of_birth, phone

---

## Module 9 - Class, Object, and initializer

---
Write a program that calculates price of an order based on the coffee type and the number of cups ordered. The program includes a class named Coffee whose constructor takes coffee type and the number of cups as arguments. The price per cup of the coffee type is predefined and stored in the class. If the coffee type is not found, the program will use a default price not return an error message. 
The methods that the class should include:
- **total_price**: calculates and returns the total price of the oder
- **price_vat**: calculates and returns the total price with a given tax percentage (13.5 %)
- **add_cups** : adds the number of cups to the order and recalculate the total price
- **__str__** method: prints the summary of the order, coffee type, number of cups, price per cup and total price

---

Write a program that: 
- Checks whether the classroom is empty
- Prints the info of the classroom´s people
- If there are people, it will find out who is the highest and remove that person from the room

---

Write a program that allows user to manage a to-do-list by the following options:
- Adds a new task
- Shows the task with priority
- Removes a task  
- Quits the program
The program should keep show the above options until the user chooses to quit. If the user tries to check the task list when it is empty, the program prints a message "You are free! To-do-list is empty".

---


## Module 10 - Association 
## Module 11 - Inheritance
## Module 12 - Programme Structure: Modules and Packages
## Module 13 - File Handling 


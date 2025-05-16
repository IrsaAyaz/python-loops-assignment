#Task 1: Using a for Loop
for i in range (1, 11):
    print(i)

#Task 2: Using a while Loop
i = 1
while i <= 5:
    print(i)
    i += 1

#Task 3: Loop with a Condition
number = int(input("Enter a Number: "))

while number >= 1:
    print(number)
    number = number - 1

#Task 4: Nested Loop
line_number = 1

for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{line_number}. {i} * {j} = {result}")
        line_number += 1

#Task 5: Using break
for number in range(0, 11):
    if number == 6:
        break
    print(number)

#Task 6: Using continue
for number in range(6):
    if number == 3:
        continue
    print(number)

word = input("Enter a word: ")

for letter in word:
    print(letter)
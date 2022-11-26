# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# Write code that opens "name.txt" and reads the name (as above) then prints, Your name is Bob".
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# Write code that opens "numbers.txt", reads only the first two numbers and adds them together
# then prints the result, which should be... 59.
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Task 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
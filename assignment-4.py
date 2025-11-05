# Task 1: Read a File and Handle Errors
try:

    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")



## Task 2: Write and Append Data to a File
input = input("Enter some data: ")
with open("output.txt", "w") as file:
    file.write(input + "\n")
with open("output.txt", "a") as file:
    file.write("This is the appended text.\n")
with open("output.txt", "r") as file:
    print("\nFinal content of the file:")
    print(file.read())

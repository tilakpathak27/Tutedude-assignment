# Task-1: Create a Dictionary of Student Marks

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")






# Task 2: Demonstrate List Slicing

numbers = list(range(1, 11))

extracted = numbers[:5]

reversed_extracted = extracted[::-1]

print("Original list:", numbers)
print("Extracted first five elements:", extracted)
print("Reversed extracted elements:", reversed_extracted)

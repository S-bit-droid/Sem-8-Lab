students={
    "Student 1": 82,
    "Student 2": 74,
    "Student 3": 91,
    "Student 4": 67,
    "Student 5": 88,
    "Student 6": 73
}
print("Students scoring above 75:")
for name,marks in students.items():
    if marks>75:
        print(name,":",marks)

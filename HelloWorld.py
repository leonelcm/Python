#hello world
print("Hello World")

#strings
hello = "Hello".capitalize()
print(hello)

split = "hello,csv,txt".split(",")
print(split)

format = "nice to me you {0} {1}".format(hello, split[0])
print(format)

format2 = f"Hello {hello}"
print(format2)

#if
number = 5

print("aaa") if number == 5 else print("bbbb")

while number > 0:
    if number == 5:
        print(number)
    else:
        print(f"not 5: {number}")
    number=number-1

#Lists
students = []
students.append("Test")
print(students)
print(students[-1])
print("True") if "Test" in students else print("False")
print("Test" in students)
print(len(students))
del students[0]
print(students)

my_names = "Leonel Joaquim Curto Murraceira".split(" ")
print(my_names[1:])
print(my_names[1:-1])

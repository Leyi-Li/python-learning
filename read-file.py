# r for read, w for write, a for append infor to the end of the file, r+ for read and write

employee_file = open("employess.txt", "r")

# print(employee_file.readable())
# print(employee_file.read())


# print(employee_file.readline())
# print(employee_file.readline())

# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)


employee_file.close()

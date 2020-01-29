# r for read, w for write, a for append infor to the end of the file, r+ for read and write

# employee_file = open("employess.txt", "r")

# print(employee_file.readable())
# print(employee_file.read())


# print(employee_file.readline())
# print(employee_file.readline())

# print(employee_file.readlines())

# for employee in employee_file.readlines():
#     print(employee)


##############################         append new info              ####################################

# employee_file = open("employess.txt", "a")

# employee_file.write("Toby - HR")
#employee_file.write("\nKelly - Customer Service")


####################################       rewrite the whole file                     ###################################

employee_file = open("employess.txt", "w")

employee_file.write("Toby - HR")


####################################       create a new file                     ###################################

employee_file1 = open("employees1.txt", "w")

employee_file.write("Toby - HR")




employee_file1.close()

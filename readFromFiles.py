# Read Only -> open(file_name, "r")
# Write Only -> open(file_name, "w")
# Append in File -> open(file_name, "a")
# Read & Write -> open(file_name, "r+")

employee_file = open("employees.txt", "r")

# Is file readable?
print(employee_file.readable())

# Read all the data from file
print(employee_file.read())

# Read by line
print(employee_file.readline())
print(employee_file.readline())

# Read multiple lines
print(employee_file.readlines())
print(employee_file.readlines()[2])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
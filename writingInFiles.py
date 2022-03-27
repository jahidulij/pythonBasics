# employee_file = open("employees.txt", "r")
# print(employee_file.read())
#
# employee_file = open("employees.txt", "a")
# # print(employee_file.writable())
# #employee_file.write("\nToby - Human Resources")
# employee_file.write("\nKelly - Customer Service")

employee_file = open("index.html", "w")
# print(employee_file.writable())
employee_file.write("<p>This is an html file.</p>")


employee_file.close()
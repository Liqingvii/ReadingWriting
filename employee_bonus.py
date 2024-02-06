import csv

file_obj = open('employee_data.csv','r')

csv_file = csv.reader(file_obj)

next(csv_file)

for row in csv_file:
    print(f"ID: {row[0]} Name: {row[1]} Age: {row[2]} Salary: {row[3]},\
    HoursWorked: {row[4]}, Productivity: {row[5]}, Team: {row[6]}, Bonus: {row[7]}")

file_obj.close()
    




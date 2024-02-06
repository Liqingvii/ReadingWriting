import csv

file_obj = open('employee_data.csv','r')

csv_file = csv.reader(file_obj)

next(csv_file)

#Efficiency = productivity / hours_worked
high_e = list()
low_e = list()
age_20s = list()
age_30s = list()
age_40s = list()

for row in csv_file:
    age = int(row[2])
    e_factor = int(row[5]) / int(row[4])
    if e_factor > 2:
        high_e.append(row[1])
    if e_factor <1:
        low_e.append(row[1])
    if age >= 20 and age < 30:
        age_20s.append(row[1])
    if age >= 30 and age < 40:
        age_30s.append(row[1])
    if age >= 40:
        age_40s.append(row[1])

print('Highly Efficient Individuals: ')
for name in high_e:
    print(name)
print('\n')

print('Low Efficient Individuals: ')
for name in low_e:
    print(name)
print('\n')

print('Employees in their 40s')
for name in age_40s:
    print(name)
print()
print(f"Total number of employees in their 40s: {len(age_40s)}")
print('\n')

print('Employees in their 30s')
for name in age_30s:
    print(name)
print()
print(f"Total number of employees in their 30s: {len(age_30s)}")
print('\n')

print('Employees in their 20s')
for name in age_20s:
    print(name)
print()
print(f"Total number of employees in their 20s: {len(age_20s)}")

file_obj.close()
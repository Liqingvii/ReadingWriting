import csv
input_file = 'customers.csv'
output_file = 'customer_country.csv'

customer_count = 0

file_obj = open(input_file, 'r')
file_obj2 = open(output_file, 'w')

reader = csv.reader(file_obj)
writer = csv.writer(file_obj2)
next(reader)
writer.writerow(['Full name', 'Country'])

for row in reader:
    Full_name = row[1] + row[2]
    Country = row[4]
    writer.writerow([Full_name, Country])

file_obj.close()
file_obj2.close()
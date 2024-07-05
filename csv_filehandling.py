import csv

"""THis is reading from csv"""


# with open('user_data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row) 

# with open('user_data.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)


"""This is writing to csv"""

import csv


data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open('user_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(data)
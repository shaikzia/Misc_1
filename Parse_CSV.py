# Program to Read, Parse, Write CSV files
# Youtube Video - Corey Scafer
# https://www.youtube.com/watch?v=q5uM4VKywbA

import csv
import os
import shutil

new_folder = '/home/zia/Learning/DataSets/For Python/CSV/Output'
if os.path.exists(new_folder):
    shutil.rmtree(new_folder)
os.mkdir(new_folder)
# except OSError

with open('/home/zia/Learning/DataSets/For Python/CSV/100-Records/100Records.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# #   Read the rows from the CSV file
#     for line in csv_reader:
#         print(line)
    next(csv_reader)
# Write the data to a new file
    with open('/home/zia/Learning/DataSets/For Python/CSV/Output/new_100Records.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

        for line in csv_reader:
            csv_writer.writerow(line)

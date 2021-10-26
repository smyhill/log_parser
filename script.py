import sys
import os
import csv

# functions used later
def DeleteBlanks(file):
    """Deletes blank lines at the end of a file"""
    with open(file) as input_file:
        data = input_file.read().rstrip('\n')
    input_file.close()
    
    with open(file, 'w') as output_file:
        output_file.write(data)
    output_file.close()

def ReadLastLine(file,number):
    """Returns a list of the last n lines of a given file"""
    with open(file) as f:
        data = []
        for line in (f.readlines() [-number:]):
            line = line.rstrip('\n')
            data.append(line)
    return(data)

# define where to look for files for parsing, type of files, and what to label the output columns
files_location = os.path.dirname(os.path.realpath(__file__))
file_extension = '.log'
dict_labels = ['Time', 'Email', 'Rank', 'FName', 'LName', 'Pass/Fail', 'SpmLic', 'Folders']

# open csv, write col heads close the csv
output_file = open("data.csv", "a", newline='')
writer = csv.writer(output_file)
writer.writerow(dict_labels)
output_file.close()

# for each file in the defined location check if its the correct file type
# if it is then run the 2 functions and write to csv
for file in os.listdir(files_location):
    if file.endswith(file_extension):
        output_file = open("data.csv", "a", newline='')
        writer = csv.writer(output_file)
        DeleteBlanks(file=file)
        log_values = ReadLastLine(file,8)
        writer.writerow(log_values)
        output_file.close()












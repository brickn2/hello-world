# Converts a .txt file to .csv

import csv

# Identify original .txt file
filename = 'test'

# Reads original .txt file
txt = filename '.txt'
with open(txt, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)

    # Saves as .csv file
    with open('test.csv', 'w') as out_file:
        writer = csv.wrter(outfile)
        # Adds column names on top row
        writer.writerow(('rpm','thrust (N)'))
        writer.writerows(lines)
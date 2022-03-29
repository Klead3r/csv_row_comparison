import csv
import sys
import os.path

new_file = "input_new.csv"
old_file = "input_old.csv"
output_file = "output.csv"

new_file_rows = []
old_file_rows = []
diff_rows = []

sys.stdout.write('Gathering rows from input files...\n')

new_rows = 0
with open(new_file) as fin_new:
    read_new = csv.reader(fin_new)
    for row_new in read_new:
        new_file_rows.append(row_new)
        new_rows = new_rows + 1
sys.stdout.write('New file has %s rows\n' % new_rows)

old_rows = 0
with open(old_file) as fin_old:
    read_old = csv.reader(fin_old)
    for row_old in read_old:
        old_file_rows.append(row_old)
        old_rows = old_rows + 1
sys.stdout.write('Old file has %s rows\n' % old_rows)

if (os.path.isfile(output_file) == False):
    diff_rows.append(new_file_rows[0])

sys.stdout.write('\nComparing rows...\n')
rows_processed = 0
unique = 0

for row_new in new_file_rows:
    row_found = 0
    for row_old in old_file_rows:
        if (row_new == row_old):
            row_found = 1
    if (row_found == 0):
        diff_rows.append(row_new)
        unique = unique + 1
    rows_processed = rows_processed + 1
    percentage = rows_processed / new_rows * 100
    sys.stdout.write(' (%d%%) %s / %s rows compared (%d non-matched)\r' % (percentage,rows_processed,new_rows, unique))
    sys.stdout.flush()

sys.stdout.write('\n\nWriting non-matched rows to output.csv...')

with open(output_file, 'a+') as fout:
    writer = csv.writer(fout)
    writer.writerows(diff_rows)

sys.stdout.write('\nDone!\n')
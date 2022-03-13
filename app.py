import csv

new_file = "input_new.csv"
old_file = "input_old.csv"
output_path = "output.csv"

new_file_rows = []
old_file_rows = []
diff_rows = []

with open(new_file) as fin_new:
    read_new = csv.reader(fin_new)
    for row_new in read_new:
        new_file_rows.append(row_new)
with open(old_file) as fin_old:
    read_old = csv.reader(fin_old)
    for row_old in read_old:
        old_file_rows.append(row_old)

diff_rows.append(new_file_rows[0])

for row_new in new_file_rows:
    row_found = 0
    for row_old in old_file_rows:
        if (row_new == row_old):
            row_found = 1
    if (row_found == 0):
        diff_rows.append(row_new)

with open(output_path, 'w') as fout:
    writer = csv.writer(fout)
    writer.writerows(diff_rows)
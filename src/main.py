import sys
import csv

file_name = sys.argv[1]
file_path = './csv_data/%s.csv' % file_name
csv_file = open(file_path, 'r')
csv_data = csv.reader(csv_file)

header = next(csv_data)
result_file_name = './result_data/%s_hex.txt' % file_name
hex_file = open(result_file_name, 'w')

total_size = 0
for row in csv_data:
    value = int(row[3])
    size = int(row[2])
    format_spec = '0%dx' % size
    hex = format(value, format_spec)
    hex_file.write(hex)

    total_size += size
    if(total_size == 8):
        hex_file.write(' ')
    if(total_size == 16):
        hex_file.write('\n')
        total_size = 0

hex_file.close()
csv_file.close()

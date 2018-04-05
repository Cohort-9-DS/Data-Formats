
import csv
"""
#reading csv files and printing in different formats
with open('movie_metadata.csv','a') as g:
    g_csv = csv.reader(g)
    #g_csv = csv.DictReader(g)
    #headers = next(g_csv)
    print(type(g_csv))
    for row in g:
    	print(row)
    	print(type(row))

# writing csv files
header = ["Student","Age","Height"]
student_names = ["Kartik","Palakh","Jagdeesh"]
student_ages = [25,25,25]

with open('byte_students.csv','w') as csv_file:
	writer = csv.writer(csv_file,delimiter=',')
	writer.writerow(header)
	for i in student_names:
		writer.writerow([i],[j])			

#JSON
# writing to json
import json
info = {
'name' : 'Uday',
'Age' : 26
}
json_sr = json.dumps(info)
print(json_sr)

#reading from json
info = json.loads(json_sr)
print(type(info))
print(info)
"""
#if working with files instead of string, use .dump and .load

# encoding and decoding 

byte  = b'This is a byte object'
print(byte)
print(type(byte))

also_byte = '字'
print(also_byte)

list_= ["uday","uday"]
string_to_byte = bytes(list_,'utf-8')
print(string_to_byte)
print(type(string_to_byte))
byte_to_string = string_to_byte.decode()
print(byte_to_string)
print(type(byte))



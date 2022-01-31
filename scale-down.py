
import csv

def writeto(line):
        outfile.write(line)

outfile = open('covid19-july-january_2020.csv', 'w')

with open('covid19-clean1.csv', 'r', newline='') as infile:
	for line in infile:
		rowarray = line.split(',')
#		outfile.write(f'{rowarray[3]},{rowarray[25]}\n')	
		
		if '2020-07' in rowarray[0]:
			writeto(line)
		if '2020-08' in rowarray[0]:
			writeto(line)
		if '2020-09' in rowarray[0]:
			writeto(line)
		if '2020-10' in rowarray[0]:
			writeto(line)
		if '2020-11' in rowarray[0]:
			writeto(line)
		if '2020-12' in rowarray[0]:
			writeto(line)
		if '2021-01' in rowarray[0]:
			writeto(line)
		

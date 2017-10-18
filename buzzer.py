import csv
import 
while True :
	valuefile = open('state.csv')
        reader = csv.reader(valuefile)
        values = list(reader)
	if values[0][0] == 1:
		print values[0][0]

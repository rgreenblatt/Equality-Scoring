import csv
import copy
from collections import defaultdict
initialClasses = [[31, 198, 59, 183, 91, 19, 184, 50, 50, 183], [33, 95, 126, 155, 58, 22, 201, 56, 58, 131], [35, 26, 109, 152, 82, 10, 262, 49, 183, 59]]
intialStudents = [174, 155, 161]

with open('students.csv') as input1:
	reader1 = csv.DictReader(input1)
	list1 = list(reader1)
writelist = []
u = 0
for i in list1:
	u += 1
	j = 0
	h = [[], [], []]
	for key in i:
		for k in initialClasses[j]:
			p = float(copy.copy(i[key]))
#			print p
			o = copy.copy(intialStudents[j])
#			print o
			h[j].append((k)*((p)/(o)))
		j+=1
	t = []
	print(h)
	for y in range(len(h[0])):
		t.append(h[0][y]+h[1][y]+h[2][y])
	
	writelist.append([2017+u] + t)

with open('classes.csv', 'wb') as output:
	writer = csv.writer(output)
#	writer.writerow(writelist[0].keys())
	c = 0
	for row in writelist:
		writer.writerow(writelist[c])
		c = c + 1
								

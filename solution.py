import calculator as c
#import newOp as o
import copy
import csv
import optest as o
import sys
from collections import defaultdict

with open('classes.csv') as input1:
	reader1 = csv.reader(input1)
	list1 = list(reader1)

del list1[10:-1]
del list1[-1]
#print list1
#nTeach = {'Art':7, 'Bio':0, 'Chem':0, 'English':0, 'FL':0, 'Math':0, 'Music':0, 'Phys':0, 'Social': 0}
#nTeach = [0, 1, 1, 0, 1, 2, 1, 1, 0]
#test = []
#for key in nTeach:
#	test.append(nTeach[key])
#print test 
#print(c.evaluate(nTeach, list1))
s = copy.copy(o.generate())
indexer = 0
bestvalue = 1000
bestindex = 0
for i in s:
	value1 = c.evaluate(i, list1)
	if value1 < bestvalue:
		bestvalue = value1
		bestindex = indexer
	indexer+=1
	if indexer % 100000 == 0:
		print indexer
		sys.stdout.flush()
print(s[bestindex])
#print c.evaluate([0, 0, 0, 1, 1, 2, 1, 1, 0], list1)

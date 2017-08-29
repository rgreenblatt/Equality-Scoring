import copy
#import solution as s
import sys
def generate():
	numberT = 7 
	classes = 10 
	index = 0
	m = [1, 2, 2, 2, 3, 1, 3, 2, 2, 2]
	teachers = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	for i in range(numberT):
		for k in range(index+1):
			x = 0
			temp = teachers[k][:]
			for j in range(classes):
				if temp[j] < m[j]:
					if x == 0:
						teachers[k][j] += 1
						x = 1
					else:
						temp1 = copy.copy(temp)
						temp1[j]+=1
						teachers.append(copy.copy(temp1))
						index += 1

		print i
		sys.stdout.flush()
	print len(teachers)
	sys.stdout.flush()
	return teachers


			
	
	

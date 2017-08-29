#cite http://planspace.org/2013/06/21/how-to-calculate-gini-coefficient-from-raw-data-in-python/
import copy
def gini(list_of_values):
	sorted_list = sorted(list_of_values)
	height, area = 0, 0
	for value in sorted_list:
		height += value
		area += height - value / 2.
	fair_area = height * len(list_of_values) / 2.
	return (fair_area - area) / fair_area

#determines how effective a solution is
def valueFunction(giniArray):
	i = 0
	l = copy.copy(len(giniArray))
	value = 0
	for gini in giniArray:
		value += gini*(1-i/l)
		i+=1
	return value

#cTeach = {Art:1, Bio:4, Chem:3, English:5, French:1, German:1, Spanish:1, Math:6, Music:1, Phys:3, Social: 5}

#nTeach = {Art:0, Bio:0, Chem:1, English:0, French:.5, German:0, Spanish:.5, Math:2, Music:1, Phys:1, Social: 0}

def evaluate(nTeach, dataset):
	#cTeach = {'Art':1, 'Bio':4, 'Chem':3, 'English':5, 'French':1, 'German':1, 'Spanish':1, 'Math':6, 'Music':1, 'Phys':3, 'Social': 5}
	cTeach = [1, 4, 3, 5, 2, 1, 6, 1, 3, 5]
	tTeach = []
	i = 0
	for i in range(len(cTeach)):
		tTeach.append(cTeach[i] + nTeach[i])
	giniByYear = []
	#print tTeach
	for students in dataset:
		sPerT = []
		for index in range(len(students)):
			sPerT.append(float(students[index])/tTeach[index])
		giniByYear.append(gini(sPerT))
	#print giniByYear
	#with open('Exports/2001to13.csv', 'wb') as output:
	#	writer = csv.writer(output)
	#		writer.writerow("Year", "Gini")
	#			c = 0
	#			for value in giniByYear:
	#				writer.writerow([2018+c, giniByRow[c]])
	#				c = c + 1
	return valueFunction(giniByYear)


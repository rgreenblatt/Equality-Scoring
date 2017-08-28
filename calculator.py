#cite http://planspace.org/2013/06/21/how-to-calculate-gini-coefficient-from-raw-data-in-python/
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
	for gini in giniArray:
		value = value + gini

cTeach = {Art:1, Bio:4, Chem:3, English:5, French:1, German:1, Spanish:1, Math:6, Music:1, Phys:3, Social: 5}

#nTeach = {Art:0, Bio:0, Chem:1, English:0, French:.5, German:0, Spanish:.5, Math:2, Music:1, Phys:1, Social: 0}

def evaluate(nTeach):

	#something here that pulls in data (called dataset)

	tTeach = {}
	i = 0
	for key in cTeach:
		tTeach[key] = cTeach[key] + nTeach[i]
		i = i + 1
	giniByYear = []
	for students in dataSet:
		sPerT = []
		for key in students:
			sPerT.append(students[key]/tTeach[key])
		giniByYear.append(gini(sPerT))
	#with open('Exports/2001to13.csv', 'wb') as output:
	#	writer = csv.writer(output)
	#		writer.writerow("Year", "Gini")
	#			c = 0
	#			for value in giniByYear:
	#				writer.writerow([2018+c, giniByRow[c]])
	#				c = c + 1
	return valueFunction(giniByYear)


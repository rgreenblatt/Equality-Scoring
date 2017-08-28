import copy
#import calculator as c
#subset_sum(numbers, target, partial=[]):
#	s = sum(partial)
	# check if the partial sum is equals to target
#	if s == target: 
#		print "sum(%s)=%s" % (partial, target)
#	if s >= target:
#		return  # if we reach the number why bother to continue
#	for i in range(len(numbers)):
#        	n = numbers[i]
#        	remaining = numbers[i+1:]
#	       	subset_sum(remaining, target, partial + [n]) 
#if __name__ == "__main__":
#	subset_sum([3,9,8,4,5,7,10],15)
def recursiveAdd(number, g, index, times): 
	times = times - 1
	i = 0
	for i in range(number):
		if i == number -1:
			g[index][0] += 1
			print index
		else:
			temp = g[index][:]
			#print g
			#print i
			temp[i+1] +=1
			g[index+i+1] = temp[:]
			print g
#			print index+i+1
		
	if times == 0:
		return index + i + 1
	else:
		return recursiveAdd(number, g, index, times)
def generateCombinations(total, number):
	g = [None]*30#000
	f = [0]*number
	values = 0	
	for i in range(number):
		f[i] = 1
		#print values
		g[values] = f[:]
		#print f
		print g
		f[i] = 0
		#print g
		values = copy.copy(recursiveAdd(number, g, values, total-1))
		#print g
	del g[values:-1]
	del g[-1]
	#print values
	return g

r = generateCombinations(3, 3)
#del r[values: -1]
print (r)
	

				

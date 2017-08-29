import copy
import sys
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
def recursiveAdd(number, g, index, times, total): 
	times = times - 1
	i = 0
	u = copy.copy(index)
	x = False
	for j in range(u): 
		for i in range(number):
			if sum(g[j]) < total:
				#print j
				#print i
				if i == 0 or x:
					if g[j][i] <2:
						g[j][i] += 1
						x = False
					else:
						x = True
						#index = index - 1
					
				else:
					temp = g[j][:]
					#print g
					#print i
					if temp[i] < 2:
						temp[i] +=1
						g[index] = temp[:]
						#print g
						index += 1
#						print index+i+1
	if times == 0:
		return index
	else:
		return recursiveAdd(number, g, index, times, total)
def generateCombinations(total, number):
	g = [None]*30000000
	f = [0]*number
	values = 0	
	for i in range(number):
		f[i] = 1
		#print values
		g[i] = f[:]
		#print f
		#print g
		f[i] = 0
		#print g
#	print g
	values = copy.copy(recursiveAdd(number, g, 3, total-1, total))
	#print g
	print "hi"
	sys.stdout.flush()
	del g[values:-1]
	del g[-1]
	#print values
	return g

r = generateCombinations(7, 11)
#del r[values: -1]
print len(r)
print(r)	

				

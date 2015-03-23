# running_median()
#
# Description:
#		- Takes the text files in the directory wc_input and sorts
#		  them alphabetically by their names into a list called FILES.
#		- Counts the number of words in each line of all the text files
#		  and stores that into a list called counter.
#		- Computes the running median by balancing a min and max heap. 
#		- Prints the medians into a text file called wc_result.
#		  The result is in wc_output directory.
# 
# Author: Reza Asad (2015)

import time
import re
import string
import heapq
from os import listdir
FILES = sorted(listdir('./wc_input'))

#---------------------------------------Running Median----------------------
def my_running_median():
	counter = []
	max_heap = []
	min_heap = []
	line_median = []
	# This creates a list called counter that stores the
	# number of words in each line of all the text files.
	for f in range(0,len(FILES)):
		with open('./wc_input/'+ FILES[f]) as text:
			for line in text:
				words = re.sub(r'[\'-._]','',line)
				words = re.findall('\w+',words)
				counter.append(len(words))
			
	num_lines = len(counter)
	line_median = [0]*num_lines

	# The first element of the running median is trivial.
	line_median[0] = counter[0]
	
	# This initializes the max and min heaps. A counter 
	# element is inserted into the max heap if it is 
	# smaller than the current median. Otherwise it
	# is inserted into the min heap.	
	if counter[1] > line_median[0]:
		heapq.heappush(min_heap,counter[1])
		heapq.heappush(max_heap,-counter[0])
	else:
		heapq.heappush(max_heap,-counter[1])
		heapq.heappush(min_heap,counter[0])
	line_median[1] = (counter[0] + counter[1])/2

	print(float(line_median[0]))
	print(float(line_median[1]))
	
	# This continues the insertion process explained above
	# but makes sure that the size of the heaps never
	# differ by more than one. If the heaps have the same
	# size the median is the average of the roots. Otherwise
	# The median is the root of the larger heap.
	for i in range(2,num_lines):
		if counter[i] > line_median[i-1]:
			heapq.heappush(min_heap,counter[i])
		else:
			heapq.heappush(max_heap,-counter[i])
			
		if len(max_heap) - len(min_heap) == 1:
			line_median[i] = -max_heap[0]
		elif len(max_heap) - len(min_heap) == -1:
			line_median[i] = min_heap[0]
		elif len(max_heap) == len(min_heap):
			line_median[i] = (min_heap[0] - max_heap[0])/2
		
		# After insertion, the size of min heap could become
		# larger than the size of the max heap by more than
		# one. In this case, remove the root of the min heap
		# and insert it into max heap. 
		elif len(max_heap) - len(min_heap) < 1:
			heapq.heappush(max_heap, -min_heap[0])
			min_heap[0] = -1
			heapq.heappop(min_heap)
			if len(max_heap) - len(min_heap) == 1:
				line_median[i] = -max_heap[0]
			elif len(max_heap) - len(min_heap) == -1:
				line_median[i] = min_heap[0]
			else:
				line_median[i] = (min_heap[0] - max_heap[0])/2
		
		# This is the reverse of the process explained above.
		elif len(max_heap) - len(min_heap) > 1:
			heapq.heappush(min_heap, -max_heap[0])
			max_heap[0] = -(10^6)
			heapq.heappop(max_heap)
			if len(max_heap) - len(min_heap) == 1:
				line_median[i] = -max_heap[0]
			elif len(max_heap) - len(min_heap) == -1:
				line_median[i] = min_heap[0]
			else:
				line_median[i] = (min_heap[0] - max_heap[0])/2
		
		# prints each median
		print(float(line_median[i]))				

#---------------------------------------Main Function-----------------------
def main():
	my_running_median()	
	
if __name__ == '__main__':
  main()
  

# word_count()
#
# Description:
#		- Takes the text files in the directory wc_input and sorts
#		  them alphabetically by their names into a list called FILES.
#		- Iterates over lines of all the text files and counts the
#		  frequency of each word.
#		- At the end, sorts the words alphabetically and prints each word
#		  and its count separated by one tab into a text file called
#		  wc_result. The result is in wc_output directory.
#
# Author: Reza Asad (2015)

import time
import re
import string
from string import ascii_letters, ascii_lowercase
from os import listdir
FILES = sorted(listdir('./wc_input'))

#--------------------------------Word Count---------------------------------
def my_word_count():
	word_count = {}
	num_files = len(FILES)
	for f in range(0,num_files):
		with open('./wc_input/'+ FILES[f]) as text:
			for line in text:
				# removing dash, apostrophe, periods and underscores
				word_list = re.sub(r'[\'-._]','',line)
				# splitting over non-alphanumeric characters
				word_list = re.findall('\w+',word_list)
				
				# converting all words to lower case
				alpha, lower = [s.encode('ascii') for s in [ascii_letters, ascii_lowercase]]
				table = bytes.maketrans(alpha, lower*2)
				word_list = [x.translate(table) for x in word_list]
				
				# counting the words in a dictionary
				for word in word_list:
					try:
						word_count[word] += 1
					except KeyError:
						word_count[word] = 1
	
	words = sorted(word_count)
	for k in words:
		print(k,'\t',word_count[k])
	text.close();
#---------------------------------------Main Function-----------------------
def main():
	my_word_count()	
		
if __name__ == '__main__':
  main()
  

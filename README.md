### Input\output
The text files in the **wc_input** directory are opened and read by **word_count.py**
and **running_median.py** in alphabetical order. The shell script **run.sh**
sets up permissions to run the python scrips and redirects the outputs
to the **wc_output** directory.

Note that I have used Python 3.5 to write the scripts. Therefore,
some of the built-in functions will not run on Python 2.

### Word Count Problem
To solve the porblem, I iterate over lines of all the text
files and count the frequency of each word. 
I first remove characters such as `'-_.` from each line.
Then I split over all the non-alphanumeric characters to produce a list
of words. The words are then kept in a dictionary called *word_count* 
and I update their counts as new words arrive. After all the files have
been processed, the words are sorted alphabetically and printed along with
their counts separated by a tab. 

### Running Median
In my solution, I count the number of words in each line of all the
text files and store the result into a list called *counter*. In order
to compute the running median, I have used a max and a min heap. Note
that python has only built-in min heap. Therefore, I created the 
max heap by inserting negative values into a min heap. 

I iterate over the values of *counter* and insert them into the heaps.
Starting from empty heaps, I take the first two values of the *counter*
and assign the smaller value to be the root of the max heap and the 
larger value to be the root of the min heap. Then the median is the average
of the root values. The insertion process continues with the following two 
constraints: 

* The new *counter* value is inserted to the max heap if it is less than
 or equal to the current median. Otherwise, it is inserted to the min heap.
* The size of the heaps should not differ by more than one. If the size of the
  heaps differs by more than one the root of the larger heap is removed and
  inserted into the smaller heap.

In this setting, if the size of the heaps are equal the median is the average
of their roots. Otherwise, the median is the root of the larger heap. 

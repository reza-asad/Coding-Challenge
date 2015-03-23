### Input\output
The text files in **wc_input** directory are opened and read by **word_count.py**
and **running_median.py** in alphabetical order. The shell script run.sh
sets up permissions to run the python scrips and redirects the outputs
to the **wc_output** directory.

Note that I have used Python 3.5 to write the scripts. Therefore,
some of the built-in functions will not run on Python 2.

### Word Count Problem
To solve the porblem I iterate over lines of all the text
files and counts the frequency of each word. In order to find the
words, first I remove characters such as `'-_.` from each line.
Then I split over the non-alphanumeric characters. The words are
then kept in a dictionary called *word_count* and I update their counts
as new words arrive. After all the files have been processed, the words
are sorted alphabetically and printed along with their counts separated
by a tab. The results are outputted into a text file called **wc_result**. 
This is in **wc_output** directory.

### Running Median
In my solution, I count the number of words in each line of all the
text files and store the result into a list called *counter*. In order
to compute the running median, I have used a max and a min heap. Note
that python has only a built-in min heap. Therefore, I created the 
max heap by inserting negative values into a min heap. 

I iterate over the values of *counter* and insert them into the heaps.
Starting from empty heaps, I take the first two values of the *counter*
and assign the smaller value to be the root of the max heap and the 
larger value to be the root of the min heap. Then the median is the average
of the root values. The isertion process continues with the following two 
constraints: 
* the new *counter* value is inserted to the max heap if it is smaller
 than the current median. 
each insertion the 
Computes the running median by balancing a min and max heap. 
Prints the medians into a text file called wc_result.
The result is in wc_output directory.

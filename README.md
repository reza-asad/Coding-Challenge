### Word Count Problem
The solution takes the text files in the directory **wc_input** and
sorts them alphabetically by their names into a list
called *FILES*. Furthermore it iterates over lines of all the text
files and counts the frequency of each word. In order to find the
words, first I remove characters such as `'-_.` from each line.
Then I split over the non-alphanumeric characters. The words are
then kept in a dictionary called *word_count* and I update their counts
as new wors arrive. After all the files have been processed, the words
are sorted  alphabetically and printed along with their counts separated.
by a tab. The results is outputted into a text file called **wc_result**. 
This is in **wc_output** directory.

### Running Median

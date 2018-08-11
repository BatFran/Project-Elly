#This is the main python code that will perform the analysis on Tolstoy's Diaries, Vol. 2
#Francisco Orejarena - franciscoeorejarena0621@gmail.com

#Importing the pandas package in Python
import pandas as pd

#Created a  variable called "raw" to read the raw text file through the command prompt
raw = pd.read_csv("raw_gutenberg_tolstoy_1895.txt", 
					encoding = 'utf-8', 
					sep = '\n', 
					error_bad_lines = False, 
					header = None,)

#Printed 'raw' by function 'head', testing whether or not the function works
print(raw.head(10))
print(len(raw))
print(raw.shape)

#August 11th, 2018: struggling with creating data frame. The good thing is that I can create an empty data frame, 
df = pd.DataFrame(eval("raw"))
tolstoy_dataframe = pd.DataFrame(data="raw", index=['orejarena', '. ', '/n'], columns=['Date', 'Place', 'Entry'], dtype=object)

print(tolstoy_dataframe)

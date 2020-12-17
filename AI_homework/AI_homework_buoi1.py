import pandas as pd
import numpy as np
import math
'''
1) Import pandas
2) Read Salaries.csv as a dataframe called sal.
3) Check the head of the DataFrame.
4) Use the .info() method to find out how many entries there
are.
5) What is the average BasePay ?
6) What is the highest amount of OvertimePay in the dataset
?
7) What is the job title of JOSEPH DRISCOLL ?
8) How much does JOSEPH DRISCOLL make (including
benefits)?
9) What is the name of highest paid person (including
benefits)?
10) What is the name of lowest paid person (including
benefits)? Do you notice something strange about how
much he or she is paid?
11) What was the average (mean) BasePay of all employees
per year? (2011-2014) ?
12) How many unique job titles are there?
13) What are the top 5 most common jobs?
14) How many Job Titles were represented by only one person
in 2013? (e.g. Job Titles with only one occurence in
2013?)
15) How many people have the word Chief in their job title?
16) Is there a correlation between length of the Job Title
string and Salary?
'''
sal = pd.read_csv("Salaries.csv")

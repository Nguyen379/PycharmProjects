"""
Bài tập hôm nay:
1. Tìm hiểu, làm trước 6 ý đầu bài SF Salaries
2. Bài tập
    giải thích tại sao truyền vào np.log mà không phải là np.log()
    Có cách nào khác để thực hiện không?
    khai báo function với def
    khai báo function lambda
    cách bí mật cực kì đơn giản :))"""
import pandas as pd
import numpy as np
import math

'''Bai 2'''
# np.log là object funtion, np.log() là function invocation
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})


def get_log(x):
    return math.log(x)


print(data)
print(data.applymap(np.log))
print(data.applymap(math.log))
print(data.applymap(lambda x: math.log(x)))
print(data.applymap(get_log))

'''Bai 1'''

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
# 2
sal = pd.read_csv("Salaries.csv")
# 3
print(sal.head())
# 4
print(sal.info())
# 5
sum_base_pay = 0
for n in sal["BasePay"].dropna():
    sum_base_pay += n
average = sum_base_pay / len(sal["BasePay"].dropna())
print(average)
# 6
largest_overtime_pay = 0
for n in sal["OvertimePay"].dropna():
    if n > largest_overtime_pay:
        largest_overtime_pay = n
print(largest_overtime_pay)

# 7, 8
a = sal.loc[sal['EmployeeName'] == "JOSEPH DRISCOLL"]
print(a["JobTitle"])
print(a["TotalPayBenefits"])

# 9
highest_paid = 0
for n in sal['TotalPayBenefits']:
    if n > highest_paid:
        highest_paid = n
b = sal.loc[sal["TotalPayBenefits"] == highest_paid]
print(b["EmployeeName"])

# 10
lowest_paid = 999999
for n in sal["TotalPayBenefits"]:
    if n < lowest_paid:
        lowest_paid = n
c = sal.loc[sal["TotalPayBenefits"] == lowest_paid]
print(c["EmployeeName"])

# 11
sum_pay_2011 = 0
division_2011 = 0
sum_pay_2012 = 0
division_2012 = 0
sum_pay_2013 = 0
division_2013 = 0
sum_pay_2014 = 0
division_2014 = 0

for n in sal["BasePay"].dropna():
    m = sal.loc[sal["BasePay"] == n]
    if m["Year"].to_string(index=False) == ' 2011':
        sum_pay_2011 += n
        division_2011 += 1
    elif m["Year"].to_string(index=False) == ' 2012':
        sum_pay_2012 += n
        division_2012 += 1
    elif m["Year"].to_string(index=False) == ' 2013':
        sum_pay_2013 += n
        division_2013 += 1
    elif m["Year"].to_string(index=False) == ' 2014':
        sum_pay_2014 += n
        division_2014 += 1
average_pay_2011 = sum_pay_2011 / division_2011
average_pay_2012 = sum_pay_2012 / division_2012
average_pay_2013 = sum_pay_2013 / division_2013
average_pay_2014 = sum_pay_2014 / division_2014

print(average_pay_2011)  # 58537.52171990339
print(average_pay_2012)  # 59596.41675378191
print(average_pay_2013)  # 61950.19791424823
print(average_pay_2014)  # 59270.32652740981
# chay mat 5 phut cuoc doi=))

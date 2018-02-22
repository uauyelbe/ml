import pandas as pd
import scipy as sc
import math

df = pd.read_csv("dataset.csv")

count = 0
for row in df.iterrows():
    count = count + 1
print(count)
c = 0
c_f_yes = 0
c_f_no = 0
c_m_yes = 0
c_m_no = 0

c_y = 0
c_n = 0

#counts yes no for gender
def gender(c_f_yes, c_f_no, c_m_yes, c_m_no, c_y, c_n, c):
    for i in range(count):
        output = df.loc[i][1]
        target = df.loc[i][20]
        c = c + 1

        if output == "Female" and target == "Yes":
            c_f_yes = c_f_yes + 1
        elif output == "Female" and target == "No":
            c_f_no = c_f_no + 1
        elif output == "Male" and target == "Yes":
            c_m_yes = c_m_yes + 1
        elif output == "Male" and target == "No":
            c_m_no = c_m_no + 1

        if target == "Yes":
            c_y = c_y + 1
        else:
            c_n = c_n + 1
    sum = c_y + c_n
    print("female churned:", c_f_yes)
    print("famele stayed:", c_f_no)
    print("male churned:", c_m_yes)
    print("male stayed:", c_m_no)
    return sum

print(gender(c_f_yes, c_f_no, c_m_yes, c_m_no, c_y, c_n, c))

#count yes no for seniorCitizen
def seniorCitizen(c_f_yes, c_f_no, c_m_yes, c_m_no, c_y, c_n):
    for i in range(count):
        output = df.loc[i][2]
        target = df.loc[i][20]

        if output == 0 and target == "Yes":
            c_f_yes = c_f_yes + 1
        elif output == 0 and target == "No":
            c_f_no = c_f_no + 1
        elif output == 1 and target == "Yes":
            c_m_yes = c_m_yes + 1
        elif output == 1 and target == "No":
            c_m_no = c_m_no + 1

        if target == "Yes":
            c_y = c_y + 1
        else:
            c_n = c_n + 1
    sum = c_y + c_n
    print("non Senior Citizen churned:", c_f_yes)
    print("non Senior Citizen stayed:", c_f_no)
    print("Senior Citizen churned:", c_m_yes)
    print("Senior Citizen stayed:", c_m_no)
    return sum

print(seniorCitizen(c_f_yes, c_f_no, c_m_yes, c_m_no, c_y, c_n))

'''
print(c_y)
print(c_n)

print(sum)

print("Number of yes female:", c_f_yes)
print("Number of no female:", c_f_no)
print("Number of yes male:", c_m_yes)
print("Number of no male:", c_m_no)
print(c)
'''
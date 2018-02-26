import pandas as pd
import scipy as sc
import math
from collections import Counter

df = pd.read_csv("dataset.csv")
column_name = df.columns.values.tolist()

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

#counts genders
def gender(c_f_yes, c_f_no, c_m_yes, c_m_no):
    for i in range(count):
        output = df.loc[i][1]
        target = df.loc[i][20]

        if output == "Female":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "Male":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

    print("female churned:", c_f_yes)
    print("female stayed:", c_m_no)
    print("male churned:", c_m_yes)
    print("male stayed:", c_f_no)

print(gender(c_f_yes, c_f_no, c_m_yes, c_m_no))

#counts senior citizens
def seniorCitizen(c_f_yes, c_f_no, c_m_yes, c_m_no):
    for i in range(count):
        output = df.loc[i][2]
        target = df.loc[i][20]

        if output == 1:
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == 0:
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

    print("non Senior Citizen churned:", c_m_yes)
    print("non Senior Citizen stayed:", c_f_no)
    print("Senior Citizen churned:", c_f_yes)
    print("Senior Citizen stayed:", c_m_no)

print(seniorCitizen(c_f_yes, c_f_no, c_m_yes, c_m_no))

#counts partners
def partner(c_f_yes, c_f_no, c_m_yes, c_m_no):
    for i in range(count):
        output = df.loc[i][3]
        target = df.loc[i][20]

        if output == "Yes":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "No":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

    print("partner and churned:", c_f_yes)
    print("not partner and stayed:", c_f_no)
    print("not partner and churned:", c_m_yes)
    print("partner and stayed:", c_m_no)

print(partner(c_f_yes, c_f_no, c_m_yes, c_m_no))

#counts dependents
def dependents(c_f_yes, c_f_no, c_m_yes, c_m_no):
    for i in range(count):
        output = df.loc[i][4]
        target = df.loc[i][20]

        if output == "Yes":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "No":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

    print("dependent and churned:", c_f_yes)
    print("not dependent and stayed:", c_f_no)
    print("not dependent and churned:", c_m_yes)
    print("dependent and stayed:", c_m_no)

print(dependents(c_f_yes, c_f_no, c_m_yes, c_m_no))

#counts phone service
def phoneService(c_f_yes, c_f_no, c_m_yes, c_m_no):
    for i in range(count):
        output = df.loc[i][6]
        target = df.loc[i][20]

        if output == "Yes":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "No":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

    print("has phone and churned:", c_f_yes)
    print("doesn't have phone and stayed:", c_f_no)
    print("doesn't have phone and churned:", c_m_yes)
    print("has phone and stayed:", c_m_no)

print(phoneService(c_f_yes, c_f_no, c_m_yes, c_m_no))

c3 = 0
c4 = 0
#counts multiple lines
def multipleLines(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4):
    for i in range(count):
        output = df.loc[i][7]
        target = df.loc[i][20]

        if output == "Yes":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "No":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

        if output == "No phone service":
            if target == "Yes":
                c3 = c3 + 1
            else:
                c4 = c4 + 1

    print("has multiple lines and churned:", c_f_yes)
    print("doesn't have multiple lines and stayed:", c_f_no)
    print("doesn't have multiple lines and churned:", c_m_yes)
    print("has multiple lines and stayed:", c_m_no)
    print("no phone service and churned:", c3)
    print("no phone service and stayed:", c4)

print(multipleLines(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4))

#counts internet service
def internetService(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4):
    for i in range(count):
        output = df.loc[i][8]
        target = df.loc[i][20]

        if output == "DSL":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "Fiber optic":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

        if output == "No":
            if target == "Yes":
                c3 = c3 + 1
            else:
                c4 = c4 + 1

    print("DSL and churned:", c_f_yes)
    print("DSL and stayed:", c_m_no)
    print("fiber optics and churned:", c_m_yes)
    print("fiber optics and stayed:", c_f_no)
    print("no internet service and churned:", c3)
    print("no internet service and stayed:", c4)

print(internetService(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4))

index = 0
#counts from index 9 to 14 columns
def index_9_to_14(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4, index):
    for index in range(index + 9, 15):
        for i in range(count):
            output = df.loc[i][index]
            target = df.loc[i][20]

            if output == "No":
                if target == "Yes":
                    c_f_yes = c_f_yes + 1
                else:
                    c_m_no = c_m_no + 1

            if output == "Yes":
                if target == "Yes":
                    c_m_yes = c_m_yes + 1
                else:
                    c_f_no = c_f_no + 1

            if output == "No internet service":
                if target == "Yes":
                    c3 = c3 + 1
                else:
                    c4 = c4 + 1

        print("===================", column_name[index], "===================")
        print("doesn't have service and churned:", c_f_yes)
        print("doesn't have service and stayed:", c_m_no)
        print("has service and churned:", c_m_yes)
        print("has service and stayed:", c_f_no)
        print("no internet service and churned:", c3)
        print("no internet service and stayed:", c4)
        c_f_yes = c_f_no = c_m_yes = c_m_no = c3 = c4 = 0

print(index_9_to_14(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4, index))

#count contracts
def contract(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4):
    for i in range(count):
        output = df.loc[i][15]
        target = df.loc[i][20]

        if output == "Month-to-month":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "One year":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

        if output == "Two year":
            if target == "Yes":
                c3 = c3 + 1
            else:
                c4 = c4 + 1

    print("Month-to-month and churned:", c_f_yes)
    print("Month-to-month and stayed:", c_m_no)
    print("One year and churned:", c_m_yes)
    print("One year and stayed:", c_f_no)
    print("Two year service and churned:", c3)
    print("Two year service and stayed:", c4)

print(contract(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4))

#counts paperless billing
def paperlessBilling(c_f_yes, c_f_no, c_m_yes, c_m_no):
    for i in range(count):
        output = df.loc[i][16]
        target = df.loc[i][20]

        if output == "Yes":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "No":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

    print("paperless billing and churned:", c_f_yes)
    print("paperless billing and stayed:", c_m_no)
    print("not paperless billing and churned:", c_m_yes)
    print("not paperless billing and stayed:", c_f_no)

print(paperlessBilling(c_f_yes, c_f_no, c_m_yes, c_m_no))

c5 = c6 = 0
#counts payment method
def paymentMethod(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4, c5, c6):
    for i in range(count):
        output = df.loc[i][17]
        target = df.loc[i][20]

        if output == "Electronic check":
            if target == "Yes":
                c_f_yes = c_f_yes + 1
            else:
                c_m_no = c_m_no + 1

        if output == "Mailed check":
            if target == "Yes":
                c_m_yes = c_m_yes + 1
            else:
                c_f_no = c_f_no + 1

        if output == "Bank transfer (automatic)":
            if target == "Yes":
                c3 = c3 + 1
            else:
                c4 = c4 + 1

        if output == "Credit card (automatic)":
            if target == "Yes":
                c5 = c5 + 1
            else:
                c6 = c6 + 1

    print("Electronic check and churned:", c_f_yes)
    print("Electronic check and stayed:", c_m_no)
    print("Mailed check and churned:", c_m_yes)
    print("Mailed check and stayed:", c_f_no)
    print("Bank transfer and churned:", c3)
    print("Bank transfer and stayed:", c4)
    print("Credit card and churned:", c5)
    print("Credit card and stayed:", c6)

print(paymentMethod(c_f_yes, c_f_no, c_m_yes, c_m_no, c3, c4, c5, c6))

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

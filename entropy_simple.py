import pandas as pd
import math
import scipy as sc

def get_data():
    df = pd.read_csv("dataset.csv")
    return df

df = get_data()

def entropy(pi):
    total = 0
    for p in pi:
        p = p/sum(pi)
        if p != 0:
            total = total - p*math.log2(p)
        else:
            total = total + 0
    return total

def gain(d, a):
    total = 0
    for v in a:
        total = total + sum(v)/sum(d)*entropy(v)
    gain = entropy(d) - total
    return gain, round(total, 2)

churn = [1869, 5174] #churn and not
gender = [
    [939, 2549], #female
    [930, 2625]  #male
]



print(gain(churn, gender)) #entropy for gender
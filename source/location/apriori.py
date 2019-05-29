import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

a_igis = pd.read_csv(r"C:\\Users\\shaliram\\pro\\findlocation\\c_igis_a.csv", header = None)
a_igis.head()
records = []
for i in range(0,1000):
    records.append([str(a_igis.values[i,j]) for j in range(0,8)])

assoc_rules = apriori(records, min_support = 0.000045, min_confidence = 0.2, min_lift = 1, min_length = 1)
assoc_results = list(assoc_rules)

print(len(assoc_results))
for item in assoc_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + str(items[0]) + " -> " + str(item[2][0][1]) )
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("==================================================")
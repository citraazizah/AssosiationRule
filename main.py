#%%
import pandas as pd 
import numpy as np
from apyori import apriori
import csv

data_market = list()
with open('dataset/market.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for baca_item in reader:
        data_market.append(baca_item)
    csvfile.close()

association_rule = apriori(data_market, min_support = 0.3, min_confidence = 0.5)
association_result = list(association_rule)

print(data_market)

print("=== ASSOCIATION RULE ===")
for item in association_result:
    pair = item[0]
    new_item = [x for x in pair]
    if len(new_item) < 2:
        print("Rule : " + new_item[0], end = " ")
    else:
        print("Rule : " + new_item[0], end = " ")
        for rule_item in new_item[1:]:
            print("->" + rule_item, end = " ")
    
    print("Nilai Support : "+str(item[1]))
    print("Nilai Confidence : "+str(item[2][0][2]))

    print("===================================================")
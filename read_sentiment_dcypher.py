import pandas as pd
from collections import Counter

df = pd.read_json(r"C:\Users\black\OneDrive\Desktop\Alex\github_projects\belgium\data\belgium_farnese5.json")
print(1)

array_sent = []
for elem in df.sentiment:
    print(elem['score'])
    array_sent.append(elem['score'])
final_dict = Counter(array_sent)


print(2)
import treetaggerwrapper
import pandas as pd
import os
import re
from nltk.corpus import wordnet as wn
from nltk.tokenize.api import StringTokenizer

tester = "tagger"
def substitute(df,series, dict):
    string_list = re.split(",| ",series)
    corpus_list=[]
    for word in string_list:
        if word in dict.keys():
            corpus_list.append(dict[word])
        else:
            corpus_list.append(word)
    corpus = ' '.join(corpus_list)
    df.testo = pd.Series(corpus)
    return df
df = pd.read_csv(os.getcwd()+r'/data/lettera_db.csv',header=0,sep=";")
df_dict = pd.read_csv(os.getcwd()+r'/data/dizionario.csv',header=0,sep=";",encoding='cp1252')
dict = df_dict.set_index('key')['value'].to_dict()
tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
for i in range(df.shape[0]):
    df_tagged = substitute(df=df.iloc[i,:].to_frame().reset_index(),series=df.loc[i,"testo"],dict=dict)
    tags = tagger.tag_text(df_tagged.testo.values)
    tags2 = treetaggerwrapper.make_tags(tags)
    df_tags= pd.DataFrame.from_records(tags2,columns=['word','pos','lemma'])
    df_tags.to_excel(os.getcwd()+r"/output/lettera"+str(i)+".xlsx",index=False)
    del tags
    del tags2
    del df_tagged

print("end program")
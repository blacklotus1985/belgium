import treetaggerwrapper
import pandas as pd
import os
import re
from nltk.corpus import wordnet as wn
from nltk.tokenize.api import StringTokenizer
#import it_core_news_sm
from sentita import calculate_polarity
import string
import re
#nlp = it_core_news_sm.load()

#  "nlp" Objectis used to create documents with linguistic annotations.
#docs = nlp(u"All is well that ends well.")

farnese = False

tester = "tagger"
def substitute(series_df,series,dict):
    string_list = re.split(",| ",series)
    corpus_list=[]
    for word in string_list:
        if word in dict.keys():
            corpus_list.append(dict[word])
        else:
            corpus_list.append(word)
    corpus = ' '.join(corpus_list)
    # remove digits from text
    remove_digits = str.maketrans('', '', string.digits)
    corpus = corpus.translate(remove_digits)
    # remove punctuation
    corpus = corpus.translate(str.maketrans('', '', string.punctuation))
    # remove parenthesis
    corpus = re.sub('[[]]', '', corpus)
    # remove digits
    corpus = re.sub(" \d+", " ", corpus)


    series_df.testo = corpus
    return series_df
df = pd.read_csv(os.getcwd()+r'/data/metadati.csv',header=0,sep=";")
df_dict = pd.read_csv(os.getcwd()+r'/data/dizionario.csv',header=0,sep=";",encoding='cp1252')
dict = df_dict.set_index('key')['value'].to_dict()
tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
clean_text = []
count = 1
for i in range(df.shape[0]):
    print(count)
    count = count +1
    if  isinstance(df.loc[i,"testo"],str):
        cleaned_series = substitute(series_df=df.iloc[i,:],series=df.loc[i,"testo"],dict=dict)
        dict_clean = {"id_lettera":cleaned_series.loc["id_lettera"], "testo":cleaned_series.loc["testo"]}
        clean_text.append(dict_clean)
        tags = tagger.tag_text(cleaned_series.testo)
        tags2 = treetaggerwrapper.make_tags(tags)
        dict_list_t=dict_clean['testo']
        df_tags= pd.DataFrame.from_records(tags2,columns=['word','pos','lemma'])
        df_tags.to_excel(os.getcwd()+r"/output/lettera"+str(i+1)+".xlsx",index=False)
        del tags
        del tags2
        del cleaned_series
cl_df = pd.DataFrame(clean_text)
if farnese:
    cl_df = cl_df.iloc[[13,14,15,16,17,18,19,20,21,22,29,30,31,32,34,36,37,38,39,40,41],:]
    cl_df.to_csv(os.getcwd()+r"/output/lettere_pulite_fnrs.csv", sep=";",columns=['id_lettera','testo'],index=False)
else:
    cl_df.to_csv(os.getcwd()+r"/output/lettere_metadati.csv", sep=";",columns=['id_lettera','testo'],index=False)

print("end program")
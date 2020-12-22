import pandas as pd
from sentita import calculate_polarity
import it_core_news_sm
sentences = ["il film era interessante"]
results, polarities = calculate_polarity(sentences)

df = pd.read_excel("/output/lettera0.xlsx",sep=";")
print(1)


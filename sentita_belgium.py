import pandas as pd
from sentita import calculate_polarity
import it_core_news_sm
sentences = ["il film era interessante",
"il cibo è davvero buono",
"il posto era davvero accogliente e i camerieri simpatici, consigliato!"]
results, polarities = calculate_polarity(sentences)

df = pd.read_excel("/output/lettera0.xlsx",sep=";")
print(1)


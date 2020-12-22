key = "d8c07403976f4a4489605d74eee79d4f"
endpoint = "https://valentsfarnese.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': endpoint,
    'Ocp-Apim-Subscription-Key': key,
}

params = urllib.parse.urlencode({
    # Request parameters
    'model-version': '{string}',
    'showStats': '{boolean}',
    'opinionMining': '{boolean}',
    'stringIndexType': '{string}',
})

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v3.1-preview.1/sentiment?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

















def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()


def sentiment_analysis_example(client):
    documents = ["Molto Illustre Signor avendo inteso che il forte di Blerich dove sta il capitano Bernabò Barboni resta con cosi poca gente senza polvere e senza viveri se non di giorno in giorno se ben mi persuado che questo non possa essere  e che Vostra Signoria poiche sa quello che conviene  e se li è¨ricordato avrà  rimediato a tutto Non posso perciÃ² lasciare di avvertirla che  sia per la reputazione come per tutto quello che può succedere  non è conveniente che stia della maniera che mi dicono quindi la prego a volersi informare bene di tutto quello che occorre in questo particolare e  stando cosi  dar ordine cosi espresso  che non ci sia mancamento perche i soldati vi possano vivere e abbiano qualche munizione di riserva  e la polvere necessaria Che per il medesimo effetto scrivo anche al cavaliere Cigogna che assista e faccia quello che conviene  e confido che quando questo non sia possa fare  avvisandomelo lei  piu volentieri darà ordine che si abbandoni e smantelli che correr rischio di ricever qualche danno  con diminuzione della reputazione E aspettando risposta  resto pregando Nostro Signor che conservi Vostra Signoria come puÃ² Di Brusselles  il 8 di marzo 1586."
]
    response = client.analyze_sentiment(documents=documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))


sentiment_analysis_example(client)
print(1)
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u"""
週刊東洋経済の特集で興味を持ち読んでみました。結論から言えば、日本経済の先行きについて実に現実的で骨太な議論を展開し、日本経済低迷の諸悪の根源である最低賃金を上げることを提案するなど、非常に読み応えがありました。外国人の視点から日本人が当たり前だと思っている思考を揺さぶってもくれます。 改めて週刊東洋経済の特集記事は、本書の魅力がまるで伝わっておらず残念すぎます。
"""
text2 = u"""
産業別に生産性を論じないと意味がないと
自分は思うのですが。確かに日本全体の生産性は
低いのですが、で自動車産業はどうでしょうか？
それも先進国最低クラスですか？
仮に最低ならそれでも世界トップなのは何故でしょう？
そういう細かい議論なしに、十把一絡げに
「日本全体に生産性が低いから、自動車産業の
生産性も上げよ。」って滅茶苦茶乱暴な議論だと
思います。そりゃ「これ以上働けないよ。」と
グチりたくもなります。
"""
#I love R&B music. Marvin Gaye is the best.\'What\'s Going On\' is one of my favorite songs. It was so sad when Marvin Gaye died.'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
document2 = types.Document(
    content=text2,
    type=enums.Document.Type.PLAIN_TEXT)


# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
sentiment2 = client.analyze_sentiment(document=document2).document_sentiment

#print('Text: {}'.format(text))
print('Sentiment-Text: {}, {}'.format(sentiment.score, sentiment.magnitude))
print('Sentiment-Text2: {}, {}'.format(sentiment2.score, sentiment.magnitude))

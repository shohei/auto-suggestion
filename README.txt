2011/9/27 青木　作成

【説明】

id：instructablesの製作記事index.htmlを格納。
# wget及びsite sucker(mac)でダウンロードした。
# instructablesの製作記事のページは、www.instructables.com/id/(記事名) にある。

parsing.py：instructablesのindex.htmlを整形してテキストファイルにする。
# BeautifulSoupが必要。
# pathを適当に変えて使ってください。

count.py：整形したテキストファイルをパースし、品詞と出現回数をカウントする。 
# 要eparser.py (佐藤さんの書いたプログラム)

count2.py：2-gramでの出力
count3.py：3-gramでの出力

porterStemmer.py：eparser.pyが読んでいる

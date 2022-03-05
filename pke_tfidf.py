import json
import sys
import jieba
from jieba import analyse

jieba.analyse.set_stop_words("data/stoplist/stoplist.txt")
keywords = analyse.extract_tags(doc, withWeight=True)
for keyword, w in keywords:
    print(keyword + str(w))

with open(str(sys.argv[1]), 'r') as test:
    for doc in json.load(test):
        tfidf = analyse.extract_tags
        keywords = tfidf(doc['news_content'])
        print(doc)
        for keyword in keywords:
            print(keyword)

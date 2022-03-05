import json
import jieba.posseg as pseg
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer

def tokenize_zh(text):
    word = []
    words = pseg.lcut(text)
    for w in words:
        word.append(w.word)
    return word

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

stop_words = stopwordslist('/home/conrad/keyword_extraction/data/stoplist/stoplist.txt')
vectorizer = CountVectorizer(tokenizer=tokenize_zh, stop_words=stop_words)
kw_model = KeyBERT()

with open('/home/conrad/keyword_extraction/data/testdata/1641197840350.json', 'r') as test:
    for doc in json.load(test):
        keywords = kw_model.extract_keywords(doc['news_content'], vectorizer=vectorizer)
        print(doc['news_content'])
        print(keywords)

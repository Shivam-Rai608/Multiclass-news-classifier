import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string as s
nltk.download('wordnet')
lemmatizer=nltk.stem.WordNetLemmatizer()

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def word_tokenize(txt):
    tokens = re.findall("[\w']+", txt)
    return tokens

def remove_stopwords(lst):
    stop=stopwords.words('english')
    new_lst=[]
    for i in lst:
        if i.lower() not in stop:
            new_lst.append(i)
    return new_lst

def remove_punctuations(lst):
    new_lst=[]
    for i in lst:
        for  j in  s.punctuation:
            i=i.replace(j,'')
        new_lst.append(i)
    return new_lst

def remove_numbers(lst):
    nodig_lst=[]
    new_lst=[]

    for i in  lst:
        for j in  s.digits:
            i=i.replace(j,'')
        nodig_lst.append(i)
    for i in  nodig_lst:
        if  i!='':
            new_lst.append(i)
    return new_lst

def lemmatzation(lst):
    new_lst=[]
    for i in lst:
        i=lemmatizer.lemmatize(i)
        new_lst.append(i)
    return new_lst

def remove_extrawords(lst):
    stop=['href','lt','gt','ii','iii','ie','quot','com']
    new_lst=[]
    for i in lst:
        if i not in stop:
            new_lst.append(i)
    return new_lst

def all_func(lst):
    e=remove_html(lst)
    e=remove_urls(e)
    e=word_tokenize(e)
    e=remove_stopwords(e)
    e=remove_punctuations(e)
    e=remove_numbers(e)
    e=lemmatzation(e)
    e=remove_extrawords(e)
    e=' '.join(e)
    return e